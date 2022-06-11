from db.run_sql import run_sql
from models.transaction import Transaction

def save(transaction):
    sql = "INSERT INTO transactions(amount, product, payer, payee) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.product.price, transaction.product, transaction.payer.id, transaction.payee.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction