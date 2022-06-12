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

    def update_first_name(self, name):
        self.first_name = name

    def update_last_name(self, name):
        self.last_name = name

    def add_to_wallet(self, charge):
        self.wallet += charge
