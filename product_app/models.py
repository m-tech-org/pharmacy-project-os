from django.db import connection

# Create your models here.

create_user_table_query = """
CREATE TABLE pharmacist (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(100)
)
"""

create_category_table_query = """
CREATE TABLE category(
    name VARCHAR(100) NOT NULL
    
)
"""

create_product_table_query = """
CREATE TABLE product(
    p_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_name VARCHAR(100) NOT NULL,
    issued_quantity INT NOT NULL,
    received_quantity INT NOT NULL,
    unit_price INT NOT NULL
)
"""

create_sale_table_query = """
CREATE TABLE sale(
    quantity INT NOT NULL,
    amount_received INT NOT NULL,
    issued_to VARCHAR(100) NOT NULL,
    unit_price INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (product_id)
    REFERENCES product (p_id)
)
"""

# create_newProduct_table_query = """
# CREATE TABLE newproduct(
#     p_id BIGINT AUTO_INCREMENT PRIMARY KEY,
#     product_name VARCHAR(100),
#     category_name VARCHAR(100),
#     received_quantity INT,
#     unit_price INT,
# )
# """

with connection.cursor() as cursor:
    cursor.execute(create_user_table_query)
    cursor.execute(create_category_table_query)
    cursor.execute(create_product_table_query)
    cursor.execute(create_sale_table_query)
    #cursor.execute(create_newProduct_table_query)
    connection.commit()
     
