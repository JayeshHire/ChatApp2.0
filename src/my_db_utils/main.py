
#class useful for operations on tables
class Table:

    def __init__(self, conn):
        self.conn = conn

    #kwargs = { column_name : data_type }
    def create_table(self, table_name, **kwargs):
        query = (f"create table {table_name} "
                 f"( ")
        col_dtype = [f"{column} {data_type}" for column, data_type in kwargs.items()]
        query += ' ,'.join(col_dtype)
        query += " )"
        return query


