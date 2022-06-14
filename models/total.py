from itertools import product


class Total:
    
    def __init__(self, total_paid, user=None, merchant=None, tag=None, product=None):
        self.total_paid = total_paid
        self.user = user
        self.merchant = merchant
        self.tag = tag
        self.product = product