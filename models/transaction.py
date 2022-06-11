class Transaction:

    def __init__(self, amount, product, payer, payee, tag, id=None):
        self.amount = amount
        self.product = product
        self.payer = payer
        self.payee = payee
        self.id = id
        self.tag = tag

    def money_transfer(self):
        self.payer.pay_for_goods(self.amount)
        # use many to many db HERE to update totals from totals repo