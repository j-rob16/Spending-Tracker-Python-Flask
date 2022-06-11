from db.run_sql import run_sql
from models.transaction import Transaction

def save(transaction):
    sql = "INSERT INTO transactions( product_id, user_id, merchant_id, tag_id ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)