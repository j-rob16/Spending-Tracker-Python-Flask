from db.run_sql import run_sql
from models.transaction import Transaction
from models.total import Total

import repositories.user_repository as user_repo
import repositories.product_repository as product_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

def save(transaction):
    sql = "INSERT INTO transactions( price, product_id, user_id, merchant_id, tag_id ) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [transaction.product.price, transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        product = product_repo.select(row['product_id'])
        price = product.price
        user = user_repo.select(row['user_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(price, product, user, merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        product = product_repo.select(result['product_id'])
        price = product.price
        user = user_repo.select(result['user_id'])
        merchant = merchant_repo.select(result['merchant_id'])
        tag = tag_repo.select(result['tag_id'])
        transaction = Transaction(price, product, user, merchant, tag, result['id'])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET ( price, product_id, user_id, merchant_id, tag_id ) = ( %s, %s, %s, %s, %s ) WHERE id = %s"
    values = [transaction.product.price, transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id]
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

# create function to cycle through database of transactions and add up 

def get_total():
    sql = "SELECT SUM( price ) FROM transactions"
    sum = run_sql(sql)[0][0]
    total = Total(sum)
    return total

def get_user_total(user):
    sql = "SELECT SUM ( price ) FROM transactions WHERE id = %s"
    values = [user.id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum, user)
    return total

def get_merchant_total(merchant):
    sql = "SELECT SUM ( price ) FROM transactions WHERE id = %s"
    values = [merchant.id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum, None, merchant)
    return total

def get_tag_total(tag):
    sql = "SELECT SUM ( price ) FROM transactions WHERE id = %s"
    values = [tag.id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum, None, None, tag)
    return total

def get_product_total(product):
    sql = "SELECT SUM ( price ) FROM transactions WHERE id = %s"
    values = [product.id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum, None, None, None, product)
    return total