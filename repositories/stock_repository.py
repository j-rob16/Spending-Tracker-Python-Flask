import imp
from db.run_sql import run_sql
from models.stock import Stock

def save(stock):
    sql = "INSERT INTO stocks( product_id, merchant_id ) VALUES ( %s, %s ) RETURNING id"
    values = [stock.product.id, stock.merchant.id]
    results = run_sql(sql, values)
    stock.id = results[0]['id']
    return stock

def delete_all():
    sql = "DELETE FROM stocks"
    run_sql(sql)