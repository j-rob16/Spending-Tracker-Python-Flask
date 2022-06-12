from flask import Flask, request, render_template, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repo

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('/transactions')
def transactions():
    all_transactions = transaction_repo.select_all()
    return render_template('/transactions/index.html', transactions=all_transactions)