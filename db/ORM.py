import sqlite3

class ORM:
    def __init__(self, name = ''):
        self.conn = sqlite3.connect(name)
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    # noJIy4aTb 3anucu
    def getData(self, name):
        return self.c.execute('SELECT * FROM ' + name)

    # noJIUy4aTb ogHy 3anucb
    def getValue(self, name):
        return self.c.execute('SELECT * FROM ' + name).fetchall()

    # u3MeH9Tb cTpoky
    # def getUpdate() 

    # # ygaJI9Tb cTpoky 
    # def getDelete()

    # #go6aBuTb 3anucb  
    # def getInsert()