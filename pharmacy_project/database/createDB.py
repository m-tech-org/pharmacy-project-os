from getpass import getpass
from mysql.connector import connect, Error

# to create the DB
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE pharmacydb"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

# to show the DB
show_db_query = "SHOW DATABASES"
with connection.cursor() as cursor:
     cursor.execute(show_db_query)
     for db in cursor:
         print(db)


# to show the DB with tables
show_table_query = "DESCRIBE movies"
with connection.cursor() as cursor:
     cursor.execute(show_table_query)
     # Fetch rows from last executed query
     result = cursor.fetchall()
     for row in result:
         print(row)