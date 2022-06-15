from flask import Flask, request, render_template, redirect
from flask import Blueprint

from models.product import Product
import repositories.product_repository as product_repo
import repositories.transaction_repository as transaction_repo

products_blueprint = Blueprint('products', __name__)

@products_blueprint.route('/products')
def products():
    all_products = product_repo.select_all()
    return render_template('products/index.html', products=all_products)

@products_blueprint.route('/products/<id>')
def show_product(id):
    product = product_repo.select(id)
    total = transaction_repo.get_product_total(id)
    transactions = transaction_repo.get_product_transactions(product)
    print(total.total_paid)
    return render_template('/products/product.html', product=product, total=total, transactions=transactions)

@products_blueprint.route('/products/new')
def new_product():
    return render_template('/products/new.html')

@products_blueprint.route('/products', methods=['POST'])
def create_product():
    name = request.form['name']
    price = request.form['price']
    product = Product(name, price)
    product_repo.save(product)
    return redirect('/merchants')

@products_blueprint.route('/products/<id>/edit')
def edit_product(id):
    product = product_repo.select(id)
    return render_template('/products/edit.html', product=product)

@products_blueprint.route('/products/<id>', methods=['post'])
def update_product(id):
    name = request.form['name']
    price = request.form['price']
    product = Product(name, price, id)
    product_repo.update(product)    
    return redirect('/merchants')

@products_blueprint.route('/products/<id>/delete')
def delete_product(id):
    product_repo.delete(id)
    return redirect('/merchants')