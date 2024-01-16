import pyodbc
class MSSQLConnection:
    def __init__(self, drive = 'SQL Server',
                        server = 'DESKTOP-CAMHONG',
                        database = 'QLTV',
                        username = '',
                        password = ''):
        self.drive = drive
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(f'DRIVER={self.drive};'
                                             f'SERVER={self.server};'
                                             f'DATABASE={self.database};'
                                             f'UID={self.username};'
                                             f'PWD={self.password}')
            print("connect successful")
            return self.connection  # Return the connection object
        except pyodbc.Error as e:
            print("Error in connection", e)
    def query(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        return cur.fetchall()

    def update(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()

    def insert(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()

    def delete(self, sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()
    def close(self):
        if  self.connection:
            self.connection.close()
            print("Connection closed")
