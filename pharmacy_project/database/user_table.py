from getpass import getpass
from database import connection


create_user_table_query = """
CREATE TABLE users(
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    collection_in_mil INT
)
"""

create_Category_table_query = """
CREATE TABLE users(
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    collection_in_mil INT
)
"""

create_Product_table_query = """
CREATE TABLE users(
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    collection_in_mil INT
)
"""

create_Sale_table_query = """
CREATE TABLE users(
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    collection_in_mil INT
)
"""

create_newProduct_table_query = """
CREATE TABLE users(
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    collection_in_mil INT
)
"""

with connection.cursor() as cursor:
    cursor.execute(create_user_table_query)
    cursor.execute(create_Category_table_query)
    cursor.execute(create_Product_table_query)
    cursor.execute(create_Sale_table_query)
    cursor.execute(create_newProduct_table_query)
    connection.commit()
