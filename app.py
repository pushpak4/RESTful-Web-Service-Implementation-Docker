import psycopg2
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)
db_connection = psycopg2.connect(
    host='postgres',
    port='5432',
    dbname='your_database',
    user='your_user',
    password='your_password'
)

def tables_exist():
    cursor = db_connection.cursor()
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'customers')")
    customers_table_exists = cursor.fetchone()[0]
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'orders')")
    orders_table_exists = cursor.fetchone()[0]
    cursor.close()
    return customers_table_exists and orders_table_exists

# Function to execute schema.sql
def execute_schema():
    cursor = db_connection.cursor()
    with open('schema.sql', 'r') as file:
        cursor.execute(file.read())
    db_connection.commit()
    cursor.close()

# Check if tables exist, if not, execute schema.sql
if not tables_exist():
    execute_schema()

@app.route('/customers')
def get_customers():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    return jsonify(customers)

@app.route('/customers/<int:customer_id>')
def get_customer(customer_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    return jsonify(customer)

@app.route('/customers/<int:customer_id>/orders')
def get_customer_orders(customer_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE customer_id = %s", (customer_id,))
    orders = cursor.fetchall()
    cursor.close()
    return jsonify(orders)

@app.route('/customers/<int:customer_id>/orders/<int:order_id>')
def get_customer_order(customer_id, order_id):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE customer_id = %s AND id = %s", (customer_id, order_id))
    order = cursor.fetchone()
    cursor.close()
    return jsonify(order)

@app.route('/')
def index():
    with open('templates/index.html', 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
