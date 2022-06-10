class Transaction:

    def __init__(self, product, payer, payee, id=None):
        self.product = product
        self.payer = payer
        self.payee = payee
        self.id = id