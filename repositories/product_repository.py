from db.run_sql import run_sql
from models.product import Product

def save(product):
    sql = "INSERT INTO products( name, price ) VALUES ( %s, %s ) RETURNING id"
    values = [product.name, product.price]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        product = Product(row['name'], row['price'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        product = Product(result['name'], result['price'], result['id'])
    return product

def update(product):
    sql = "UPDATE products SET ( name, price ) = ( %s, %s ) WHERE id = %s"
    values = [product.name, product.price, product.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)