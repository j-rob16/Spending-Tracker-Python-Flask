class Transaction:

    def __init__(self, amount, product, payer, payee, id=None):
        self.amount = amount
        self.product = product
        self.payer = payer
        self.payee = payee
        self.id = id