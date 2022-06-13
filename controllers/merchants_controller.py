from crypt import methods
from flask import Flask, request, render_template, redirect
from flask import Blueprint

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repo

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    all_merchants = merchant_repo.select_all()
    return render_template('merchants/index.html', merchants=all_merchants)

@merchants_blueprint.route('/merchants/<id>')
def show_merchant(id):
    merchant = merchant_repo.select(id)
    return render_template('/merchants/shop.html', merchant=merchant)

@merchants_blueprint.route('/merchants/new')
def new_merchant():
    return render_template('/merchants/new.html')

@merchants_blueprint.route('/merchants', methods=['POST'])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repo.save(merchant)
    return redirect('/merchants')

@merchants_blueprint.route('/merchants/<id>/edit')
def edit_merchant(id):
    merchant = merchant_repo.select(id)
    return render_template('/merchants/edit.html', merchant=merchant)

@merchants_blueprint.route('/merchants/<id>', methods=['post'])
def update_merchant(id):
    name = request.form['name']
    merchant = Merchant(name, id)
    merchant_repo.update(merchant)    
    return redirect('/merchants')