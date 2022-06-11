class Transaction:

    def __init__(self, product, user, merchant, tag, id=None):
        self.product = product
        self.user = user
        self.merchant = merchant
        self.id = id
        self.tag = tag

    def money_transfer(self):
        self.user.pay_for_goods(self.product.price)
        # use many to many db HERE to update totals from totals repo