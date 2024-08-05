class DbDataTypeMeta(type):
    def __new__(cls, name, bases, namespace):
        predefined_names = ['Boolean',
                            'Char',
                            'NumericTypes',
                            'Temporal',
                            'UUID',
                            # 'array',
                            'JSON',
                            'SpecialDataTypes',
                            'NetworkDataTypes',
                            ]
        if name not in predefined_names:
            raise ValueError(f"different name is not accepted "
                             f"it should be from this list :{predefined_names}")
        if len(bases) != 1:
            if len(bases) > 1:
                raise Exception(f"{name} can only inherit one class. "
                                f"But two were given.\n"
                                f"try removing one of the base class from {bases}")
            elif len(bases) == 1:
                if bases[0] is not DataType:
                    raise ValueError(f"All the data db_types should be extension of the DataType class")

        def callable_func(obj, db_type):
            if db_type.toLowerCase() not in obj.db_types:
                raise ValueError(f"db_type should be one of the below db_types :\
                \n{obj.db_types}")

            for key, value in obj.db_types.items():
                if db_type.toLowerCase() is key:
                    return value

        namespace['__call__'] = callable_func
        cls_obj = super().__new__(cls, name, bases, namespace)
        return cls_obj



 class DataTypeMeta(type):
     class_obj = {}
     # def __new__(cls, name, bases, namespace):



class DataType:
    pass


class Boolean(DataType, metaclass=DbDataTypeMeta):
    """
    usage:
        create an instance of boolean
        b = boolean()
        b()
        >> 'boolean'
    """
    def __call__(self):
        return 'boolean'


# meta class for Char inherited classes
# class CharMeta(db_type):
#     def __new__(cls, name, bases, namespace):
#         if len(bases) != 1:
#             raise Exception(f"'{name}' can only inherit one base class"
#                             f"and that is 'Char'") \
#                 if len(bases) > 1 else Exception(f"'{name}' should inherit from one base class 'Char'")
#         elif bases[0] is not Char:
#             raise Exception(f"{name} should inherit from only 'Char' class ")
#         #remaining to return a class object


class CharSeqType(DataType, metaclass=DbDataTypeMeta):
    # db_types = ('char', 'varchar', 'text')
    """
    usage :
        create a instance of this class
        inst = CharSeqType()
        char_inst = inst('char')
        char_inst(n)
        >> 'char(n)'
    """

    class Char:
        def __call__(self, n):
            return f"char({n})"

    class Varchar:
        def __call__(self, n):
            return f"varchar({n})"

    class Text:
        def __call__(self, n):
            return f"text"

    # def __call__(self, db_type):
    #
    #     if db_type not in self.db_types:
    #         raise  ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.toLowerCase() is key:
    #             return value

    @property
    def db_types(self):
        return {
                'char': self.Char(),
                'varchar': self.Varchar(),
                'text': self.Text(),
                }

    @db_types.setter
    def db_types(self, val):
        raise Exception("cannot change value of attribute 'db_types'."
         "It is immutable")

    # def __init__(self, sql_db_type):
    #     self._sql_db_type = sql_db_type
    #
    # @property
    # def sql_db_type(self):
    #     return self._sql_db_type
    #
    # @sql_db_type.setter
    # def sql_db_type(self, val):
    #     if val not in self.db_types:
    #         raise ValueError(f"sql db_type is not correct for Char class."
    #                          f"It should be from among these {self.db_types}")
    #     self._sql_db_type = val
    #
    # @property
    # def db_types(self):
    #     return ('char', 'varchar', 'text')
    #
    # @db_types.setter
    # def db_types(self, val):
    #     raise Exception("'db_types' attribute is immutable")
    #
    # pass


class NumericTypes(DataType, metaclass=DbDataTypeMeta):
    # _db_types = ('integer',
    #          'smallint',
    #          'bigint',
    #          'serial',
    #          'float',
    #          'numeric',
    #          )
    """
    usage :
    create an instance of NumericTypes
    nType = NumericTypes()
    numeric = nType('numeric')
    numeric(4,3)
    >> 'numeric(4,3)'
    """
    class Integer:
        def __call__(self):
            return f"integer"

    class SmallInt :
        def __call__(self):
            return f"smallint"

    class BigInt:
        def __call__(self):
            return f"bigint"

    class Serial:
        def __call__(self):
            return f"serial"

    class Float:
        def __call__(self):
            return f"float"

    class Numeric:
        def __call__(self, d, p):
            # d - digits
            # p - decimals
            return f"numeric({d},{p})"

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.toLowerCase() is key:
    #             return value


    @property
    def db_types(self):
        return {'integer': self.Integer(),
                'smallint': self.SmallInt(),
                'bigint': self.BigInt(),
                'serial': self.Serial(),
                'float': self.Float(),
                'numeric': self.Numeric(),
                }

    @db_types.setter
    def db_types(self, val):
        raise Exception("cannot change value of attribute 'db_types'."
                        "It is immutable")



class Temporal(DataType, metaclass=DbDataTypeMeta):
    # _db_types = ('date',
    #          'time',
    #          'timestamp',
    #          'timestamptz',
    #          'interval'
    #          )

    class Date:
        def __call__(self):
            return 'date'

    class Time:
        def __call__(self):
            return 'time'

    class TimeStamp :
        def __call__(self):
            return 'timestamp'

    class TimeStampTZ:
        def __call__(self):
            return 'timestamptz'

    class Interval:
        def __call__(self):
            return "interval "

    # def __call__(self, db_type):
    #
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.toLowerCase() is key:
    #             return value


    @property
    def db_types(self):
        return {'date': self.Date(),
                'time': self.Time(),
                'timestamp': self.TimeStamp(),
                'timestamptz': self.TimeStampTZ(),
                'interval': self.Interval()
                }

    @db_types.setter
    def db_types(self, val):
        raise Exception("cannot change value of attribute 'db_types'."
                        "It is immutable")


class UUID(DataType, metaclass=DbDataTypeMeta):

    def __call__(self):
        return 'uuid'

    @property
    def db_types(self):
        return 'uuid'

    @db_types.setter
    def db_types(self, val):
        raise Exception("'db_types' attribute is immutable")

    pass


class JSON(DataType, metaclass=DbDataTypeMeta):
    # _db_types = ('json', 'jsonb')


    class JSON:
        def __call__(self):
            return 'json'

    class JSONB:
        def __call__(self):
            return 'jsonb'

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.toLowerCase() is key:
    #             return value


    @property
    def db_types(self):
        return {
                'json': self.JSON(),
                'jsonb':self.JSONB()
                }

    @db_types.setter
    def db_types(self, val):
        raise Exception("'db_types' attribute is immutable")



class SpecialDataTypes(DataType, metaclass=DbDataTypeMeta):
    # _db_types = ('hstore','geometric',)


    class HStore:
        def __call__(self):
            return "hstore"

    class Geometric:
        def __call__(self):
            return "geometric"

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.toLowerCase() is key:
    #             return value

    @property
    def db_types(self):
        return {
            'hstore': self.HStore(),
            'geometric': self.Geometric()
            }

    @db_types.setter
    def db_types(self, val):
        raise Exception("'db_types' attribute is immutable")

    pass


class NetworkDataTypes(DataType, metaclass=DbDataTypeMeta):
    # _db_types = ('CIDR', 'INET', 'MACADDR')


    class CIDR:
        def __call__(self):
            return f"cidr"

    class INET:
        def __call__(self):
            return f"inet"

    class MacAddr:
        def __call__(self):
            return f"macaddr"

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.toLowerCase() is key:
    #             return value

    @property
    def db_types(self):
        return {
            'cidr': self.CIDR(),
            'inet': self.INET(),
            'macaddr': self.MacAddr()
                }

    @db_types.setter
    def db_types(self, val):
        raise Exception("'db_types' attribute is immutable")

    pass
