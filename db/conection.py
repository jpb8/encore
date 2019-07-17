import pyodbc


class Connection:
    # TODO: Build INSERT sql string function based off Columns and Table name
    TABLE_NAME = ""
    SQL_ADD = ""
    PK = ""
    COLUMNS = []

    def __init__(self, con_string):
        self.con_string = con_string
        self.cursor = pyodbc.connect(con_string)

    @property
    def pks(self):
        return [pk[0] for pk in self.cursor.execute("SELECT {} FROM {}".format(self.PK, self.TABLE_NAME)).fetchall()]

    def all(self):
        return self.cursor.execute("SELECT * FROM {}".format(self.TABLE_NAME)).fetchall()

    def add(self, values):
        return self.cursor.execute(self.SQL_ADD, values)

    def check_pk(self, pk_value):
        sql_str = "SELECT count(*) FROM {} WHERE {} = ?".format(self.TABLE_NAME, self.PK)
        data = self.cursor.execute(sql_str, pk_value).fetchone()[0]
        if data != 0:
            return False
        return True


