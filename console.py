import pdb

from models.product import Product
from models.merchant import Merchant
from models.tag import Tag
from models.total import Total
from models.transaction import Transaction
from models.user import User

import repositories.merchant_repository as merchant_repo
import repositories.product_repository as product_repo
import repositories.tag_repository as tag_repo
import repositories.total_repository as total_repo
import repositories.transaction_repository as transaction_repo
import repositories.user_repository as user_repo

tag_repo.delete_all()
total_repo.delete_all()
