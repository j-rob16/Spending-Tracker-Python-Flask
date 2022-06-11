from db.run_sql import run_sql
from models.product import Product

def save(product):
    sql = "INSERT INTO products(name, price) VALUES (%s, %s) RETURNING id"
    values = [product.name, product.price]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)