class User:

    def __init__(self, first_name, last_name, age, wallet, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.wallet = wallet
        self.id = id

    def pay_for_goods(self, amount):
        self.wallet -= amount
        # call update from user repo here
