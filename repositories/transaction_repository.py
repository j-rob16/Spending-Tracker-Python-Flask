from db.run_sql import run_sql
from models.transaction import Transaction
from models.user import User
import repositories.user_repository as user_repo
import repositories.product_repository as product_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

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
        product = product_repo.select(row['product_id'])
        user = user_repo.select(row['user_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(product, user, merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    # transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    product = product_repo.select(result['product_id'])
    user = user_repo.select(result['user_id'])
    merchant = merchant_repo.select(result['merchant_id'])
    tag = tag_repo.select(result['tag_id'])
    # if result is not None:
    transaction = Transaction(product, user, merchant, tag, result['id'])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET ( product_id, user_id, merchant_id, tag_id ) = ( %s, %s, %s, %s ) WHERE id = %s"
    values = [transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def get_user(transaction):
    user_id = transaction.user
    user = user_repo.select(user_id)
    return user
