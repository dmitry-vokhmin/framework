class Singleton(type):
    #__prepare__
    #__new__
    #__init__
    #__call__
    def __init__(cls, name, bases, attrs, **kwargs):
        # super() - <super: <class 'Singleton'>, <Singleton object>>
        super().__init__(name, bases, attrs)
        cls.__instance = None


    def __call__(cls, *args, **kwargs):
        # print(cls)
        # print(cls.__instance)
        if cls.__instance is None:
            # Через магию super().__call__
            # вызывается MySqlConnection.__new__и MySqlConnection.__init__
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class MySqlConnection(metaclass=Singleton):
    pass


sql_connection_1 = MySqlConnection()
sql_connection_2 = MySqlConnection()
sql_connection_3 = MySqlConnection()

print(sql_connection_1 is sql_connection_3)

print(sql_connection_1.__class__.__class__)

"""
<class '__main__.MySqlConnection'>
None

<class '__main__.MySqlConnection'>
<__main__.MySqlConnection object at 0x000000DC41932208>
"""
