# Project Title: 
PHARMACY INVENTORY

## Project Description
Pharmacy Inventory is an inventory manager that monitors the quantity of products in stock, generates an order summary and calculates total sales and balance received by customers for the month.

## Features
-  The user can create a database table of each item, the item category, unit price and total quantity in stock.
-  User can click on an item, buy it, and generate a receipt.
-  Within the receipt page, the total cost of the item is calculated based on the quantity purchased and the unit price.
-  The balance to be received is also calculated by subtracting the total cost from the amount paid.
-  Based on products sold, a database table of all sales made is created the keeps track of the following:
a) The total amount paid summed up for all the items sold.
b) The total balance received by all customers is also summed up.
c) Net balance after subtracting total balance received from total amout paid.
d) The app keeps a log of the quantity remaining in stock for each item as it is being sold
-  The app is also able to replenish depleting stock in the Products quantity table.

## TESTING
Username: "pharmacy", 
Password: "1234"

## Built with
- HTML
- CSS
- Bootstrap
- POSTGRESQL
- Python
- Django
- Heroku


# How to use: 
Change into the App directory:

```
$ cd pharmacy-inventory-manager
```

Run the server:
```
$ python manage.py runserver
```















