from db.run_sql import run_sql
from models.transaction import Transaction

def save(transaction):
    sql = "INSERT INTO transactions( product_id, user_id, merchant_id, tag_id ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        transaction = Transaction(row['product_id'], row['user_id'], row['merchant_id'], row['tag_id'], row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        transaction = Transaction(result['product_id'], result['user_id'], result['merchant_id'], result['tag_id'], result['id'])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET ( product_id, user_id, merchant_id, tag_id ) VALUES ( %s, %s, %s, %s ) WHERE id = %s"
    values = [transaction.product_id, transaction.user_id, transaction.merchant_id, transaction.tag_id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)