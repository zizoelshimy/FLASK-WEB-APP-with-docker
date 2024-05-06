import mysql.connector
from mysql.connector import errorcode
class Database:
    def __init__(self):
        self.result = []

    def connect(self):
        try:
            self.mydb = mysql.connector.connect(
                host="db",
                user="root", 
                password="1234",
                database="python",
                auth_plugin='mysql_native_password'
            )
            self.cursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def fetch_data(self):
        try:
            self.cursor.execute("SELECT * FROM python.users")
            self.result = self.cursor.fetchall() 
            return self.result  # Return the result as a list
        except mysql.connector.Error as err:
            print(err)