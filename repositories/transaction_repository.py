from datetime import datetime

from db.run_sql import run_sql
from models.transaction import Transaction
from models.total import Total

import repositories.user_repository as user_repo
import repositories.product_repository as product_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

def save(transaction):
    sql = "INSERT INTO transactions( price, product_id, user_id, merchant_id, tag_id, date ) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [transaction.product.price, transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id, transaction.date]
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
        transaction = Transaction(price, product, user, merchant, tag, row['date'], row['id'])
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
        transaction = Transaction(price, product, user, merchant, tag, result['date'], result['id'])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET ( price, product_id, user_id, merchant_id, tag_id, date ) = ( %s, %s, %s, %s, %s, %s ) WHERE id = %s"
    values = [transaction.product.price, transaction.product.id, transaction.user.id, transaction.merchant.id, transaction.tag.id, transaction.date]
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
    sql = "SELECT SUM ( price ) FROM transactions WHERE user_id = %s"
    values = [user.id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum)
    return total

def get_user_transactions(user):
    transactions = []
    sql = "SELECT * FROM transactions WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)
    for row in results:
        product = product_repo.select(row['product_id'])
        price = product.price
        # user = user_repo.select(row['user_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(price, product, user, merchant, tag, row['date'], row['id'])
        transactions.append(transaction)
    return transactions

def get_merchant_total(id):
    sql = "SELECT SUM ( price ) FROM transactions WHERE merchant_id = %s"
    values = [id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum)
    return total 

def get_merchant_transactions(merchant):
    transactions = []
    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)
    for row in results:
        product = product_repo.select(row['product_id'])
        price = product.price
        user = user_repo.select(row['user_id'])
        # merchant = merchant_repo.select(row['merchant_id'])
        tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(price, product, user, merchant, tag, row['date'], row['id'])
        transactions.append(transaction)
    return transactions

def get_tag_total(id):
    sql = "SELECT SUM ( price ) FROM transactions WHERE tag_id = %s"
    values = [id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum)
    return total

def get_tag_transactions(tag):
    transactions = []
    sql = "SELECT * FROM transactions WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)
    for row in results:
        product = product_repo.select(row['product_id'])
        price = product.price
        user = user_repo.select(row['user_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        # tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(price, product, user, merchant, tag, row['date'], row['id'])
        transactions.append(transaction)
    return transactions

def get_product_total(id):
    sql = "SELECT SUM ( price ) FROM transactions WHERE product_id = %s"
    values = [id]
    sum = run_sql(sql, values)[0][0]
    total = Total(sum)
    return total

def get_product_transactions(product):
    transactions = []
    sql = "SELECT * FROM transactions WHERE product_id = %s"
    values = [product.id]
    results = run_sql(sql, values)
    for row in results:
        # product = product_repo.select(row['product_id'])
        price = product.price
        user = user_repo.select(row['user_id'])
        merchant = merchant_repo.select(row['merchant_id'])
        tag = tag_repo.select(row['tag_id'])
        transaction = Transaction(price, product, user, merchant, tag, row['date'], row['id'])
        transactions.append(transaction)
    return transactions