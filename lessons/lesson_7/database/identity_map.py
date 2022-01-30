class UnitOfWork:
    # ...
    person_map = {}

    @classmethod
    def add_person(cls, person):
        if person.get_id() not in cls.person_map.keys():
            cls.person_map[person.get_id()] = person

    @classmethod
    def get_person(cls, key):
        if key in cls.person_map.keys():
            return cls.person_map[key]
        else:
            return None
