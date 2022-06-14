import pdb

from models.product import Product
from models.merchant import Merchant
from models.tag import Tag
from models.total import Total
from models.transaction import Transaction
from models.user import User

import repositories.merchant_repository as merchant_repo
import repositories.product_repository as product_repo
import repositories.stock_repository as stock_repo
import repositories.tag_repository as tag_repo
import repositories.total_repository as total_repo
import repositories.transaction_repository as transaction_repo
import repositories.user_repository as user_repo

tag_repo.delete_all()
total_repo.delete_all()
stock_repo.delete_all()
transaction_repo.delete_all()
merchant_repo.delete_all()
user_repo.delete_all()

user_1 = User('John', 'Wick', 43, 2000)
user_repo.save(user_1)

merchant = Merchant('Tesco')
merchant_repo.save(merchant)

product_1 = Product('Vegetables', 20)
product_repo.save(product_1)

tag_1 = Tag('Groceries')
tag_repo.save(tag_1)

transaction_1 = Transaction(product_1.price, product_1, user_1, merchant, tag_1)
transaction_repo.save(transaction_1)

pdb.set_trace()
