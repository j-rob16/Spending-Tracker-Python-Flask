from flask import Flask, request, render_template, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repo
import repositories.product_repository as product_repo
import repositories.tag_repository as tag_repo
import repositories.merchant_repository as merchant_repo
import repositories.user_repository as user_repo

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('/transactions')
def transactions():
    all_transactions = transaction_repo.select_all()
    return render_template('/transactions/index.html', transactions=all_transactions)

@transactions_blueprint.route('/transactions/<id>')
def show_transaction(id):
    transaction = transaction_repo.select(id)
    return render_template('/transactions/transaction.html')

@transactions_blueprint.route('/transactions/new')
def new_transaction():
    products = product_repo.select_all()
    merchants = merchant_repo.select_all()
    tags = tag_repo.select_all()
    users = user_repo.select_all()
    return render_template('/transactions/new.html', products=products, merchants=merchants, tags=tags, users=users)

@transactions_blueprint.route('/transactions', methods=['POST'])
def create_transaction():
    product_id = request.form['product_id']
    product = product_repo.select(product_id)
    merchant_id = request.form['merchant_id']
    merchant = merchant_repo.select(merchant_id)
    user_id = request.form['user_id']
    user = user_repo.select(user_id)
    tag_id = request.form['tag_id']
    tag = tag_repo.select(tag_id)
    transaction = Transaction(product, user, merchant, tag)
    transaction_repo.save(transaction)
    # add to total table
    return redirect('/transactions')