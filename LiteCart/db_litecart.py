import mysql.connector as mysql


def verify_order_in_db():
    db_orders = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database='litecart'
    )
    cursor = db_orders.cursor()

    query = "SELECT * FROM `lc_orders`"
    cursor.execute(query)
    db_orders.close()
    if len(query) > 0:
        return True
    else:
        return False


def verify_edit_first_name_in_db(f_name: str):
    db_customers = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database='litecart'
    )
    cursor = db_customers.cursor()

    query = "SELECT firstname FROM `lc_customers` WHERE ID=2"
    cursor.execute(query)
    first_name = cursor.fetchall()
    db_customers.close()
    for customers in first_name:
        first_name = customers
        if first_name == f_name:
            return True
        else:
            return False


def verify_edit_last_name_in_db(l_name: str):
    db_customers = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database='litecart'
    )
    cursor = db_customers.cursor()

    query = "SELECT lastname FROM `lc_customers` WHERE ID=2"
    cursor.execute(query)
    last_name = cursor.fetchall()
    db_customers.close()
    for customers in last_name:
        last_name = customers
        if last_name == l_name:
            return True
        else:
            return False
