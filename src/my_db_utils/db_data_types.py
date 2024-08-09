
#meta class for group of data types
class DbDataTypeMeta(type):
    _instances = {}

    def __new__(cls, name, bases, namespace):
        predefined_names = ['Boolean',
                            'CharSeqType',
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

        #this function makes the instance of the main class callable
        def callable_func(obj, db_type):
            if db_type.lower() not in obj.db_types:
                raise ValueError(f"db_type should be one of the below db_types :\
                \n{obj.db_types}")

            return obj.db_types[db_type.lower()]

        namespace['__call__'] = callable_func
        if name not in cls._instances :
            cls_obj = super().__new__(cls, name, bases, namespace)
            cls._instances[name] = cls_obj
            return cls_obj

        return cls._instances[name]


#meta class for the actual data type
class SqlDataTypeMeta(type):
        class_names = ('Char',
                       'Varchar',
                       'Numeric',
                       'Text',
                       'Integer',
                       'SmallInt',
                       'BigInt',
                       'Serial',
                       'Float',
                       'Date',
                       'Time',
                       'TimeStamp',
                       'TimeStampTZ',
                       'Interval',
                       'UUID',
                       'JSON',
                       'JSONB',
                       'HStore',
                       'Geometric',
                       'CIDR',
                       'INET',
                       'MacAddr',
                       'Boolean',
                       'UUID'
                       )

        def __new__(cls, name, bases, namespace):
            if name not in cls.class_names:
                raise ValueError(f"name of the class cannot \
                be other than these names:\n \
                                 {cls.class_names}")

            def callable_func(obj, **kwargs):
                # return_dict = {'Char': f"char({kwargs['n']})",
                #                'Varchar': f"varchar({kwargs['n']})",
                #                'Text': f"text",
                #
                #                }
                if name in cls.class_names[0:2]:
                    return f"{name.lower()}({kwargs['n']})"
                elif name is cls.class_names[2]:
                    return f"{name.lower()}({kwargs['d']}, {kwargs['p']})"
                elif name in cls.class_names[3:len(cls.class_names)]:
                    return f"{name.lower()}"

            namespace['__call__'] = callable_func
            return super().__new__(cls, name, bases, namespace)


# meta class for classes which are themselves actual data type class
# and group data type class as well
class GroupedActualDataTypeMeta(DbDataTypeMeta, SqlDataTypeMeta):
    pass

class DataTypeMeta(type):
     class_obj = {}
     # def __new__(cls, name, bases, namespace):



class DataType:
    pass


# this is an grouped as well as actual data type class
class Boolean(DataType, metaclass=GroupedActualDataTypeMeta):
    """
    usage:
        create an instance of boolean
        b = boolean()
        b()
        >> 'boolean'
    """
    def __call__(self):
        return 'boolean'

    @property
    def db_types(self):
        return 'boolean'

    @db_types.setter
    def db_types(self, val):
        raise Exception("'db_types' attribute is immutable")

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
    
    class Char(metaclass=SqlDataTypeMeta):
        # def __call__(self, n):
        #     return f"char({n})"
        pass

    class Varchar(metaclass=SqlDataTypeMeta):
        # def __call__(self, n):
        #     return f"varchar({n})"
        pass

    class Text(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"text"
        pass

    # def __call__(self, db_type):
    #
    #     if db_type not in self.db_types:
    #         raise  ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.lower() is key:
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
    # class SqlDataTypeMeta(type):
    #     def __new__(cls, name, bases, namespace):
    # 
    #         def callable_func(self, )

    class Integer(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"integer"
        pass

    class SmallInt(metaclass=SqlDataTypeMeta) :
        # def __call__(self):
        #     return f"smallint"
        pass

    class BigInt(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"bigint"
        pass

    class Serial(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"serial"
        pass

    class Float(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"float"
        pass

    class Numeric(metaclass=SqlDataTypeMeta):
        # def __call__(self, d, p):
        #     # d - digits
        #     # p - decimals
        #     return f"numeric({d},{p})"
        pass

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.lower() is key:
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

    class Date(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return 'date'
        pass

    class Time(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return 'time'
        pass

    class TimeStamp(metaclass=SqlDataTypeMeta) :
        # def __call__(self):
        #     return 'timestamp'
        pass

    class TimeStampTZ(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return 'timestamptz'
        pass

    class Interval(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return "interval "
        pass

    # def __call__(self, db_type):
    #
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.lower() is key:
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


class UUID(DataType, metaclass=GroupedActualDataTypeMeta):

    # def __call__(self):
    #     return 'uuid'

    @property
    def db_types(self):
        return 'uuid'

    @db_types.setter
    def db_types(self, val):
        raise Exception("'db_types' attribute is immutable")

    pass


class JSON(DataType, metaclass=DbDataTypeMeta):
    # _db_types = ('json', 'jsonb')


    class JSON(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return 'json'
        pass

    class JSONB(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return 'jsonb'
        pass

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.lower() is key:
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


    class HStore(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return "hstore"
        pass

    class Geometric(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return "geometric"
        pass

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.lower() is key:
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


    class CIDR(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"cidr"
        pass

    class INET(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"inet"
        pass

    class MacAddr(metaclass=SqlDataTypeMeta):
        # def __call__(self):
        #     return f"macaddr"
        pass

    # def __call__(self, db_type):
    #     if db_type not in self.db_types:
    #         raise ValueError(f"db_type should be one of the below db_types :\
    #         \n{self.db_types}")
    #
    #     for key, value in self.db_types.items():
    #         if db_type.lower() is key:
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
