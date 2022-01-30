from sqlite3 import connect


class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit error: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update error: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete error: {message}')


class PersonMapper:
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_person):
        statement = f"SELECT IDPERSON, FIRSTNAME," \
            f" LASTNAME FROM PERSON WHERE IDPERSON=?"

        self.cursor.execute(statement, (id_person,))
        result = self.cursor.fetchone()
        if result:
            return Person(*result)
        else:
            raise RecordNotFoundException(f'record with id={id_person}'
                                          f' not found')

    def insert(self, person):
        statement = f"INSERT INTO PERSON (FIRSTNAME, LASTNAME) VALUES (?, ?)"
        self.cursor.execute(statement, (person.first_name, person.last_name))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, person):
        statement = f"UPDATE PERSON SET FIRSTNAME=?, " \
            f"LASTNAME=? WHERE IDPERSON=?"
        self.cursor.execute(statement, (person.first_name, person.last_name,
                                        person.id_person))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, person):
        statement = f"DELETE FROM PERSON WHERE IDPERSON=?"
        self.cursor.execute(statement, (person.id_person,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class Person:
    def __init__(self, id_person, first_name, last_name):
        self.id_person = id_person
        self.last_name = last_name
        self.first_name = first_name


# person = Person(1, 'иван', 'иванов')
connection = connect('patterns.sqlite')
person_mapper = PersonMapper(connection)
person_1 = person_mapper.find_by_id(1)
print(person_1.__dict__)
print(type(person_1))

person_1.last_name = '1233'
person_mapper.update(person_1)
print(person_1.__dict__)
