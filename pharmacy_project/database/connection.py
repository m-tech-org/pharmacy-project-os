from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user= "admin",
        password="1234",
        database="pharmdb",
    ) as connection:
        print(connection)
except Error as e:
    print(e)