class SuperMarket:
    def __init__(self, name, code, address, date):
        self.name = name
        self.code = code
        self.address = address
        self.date = date
        self.productInS = {}


    def get_product_code(self):
        return self.product_code

        # setter method
    def set_product_code(self, product_code):
        self.product_code = product_code

    def get_name(self):
        return self.name

    # setter method
    def set_name(self, name):
        self.name = name

    def get_code(self):
        return self.code

    # setter method
    def set_code(self, code):
        self.code = code

    def get_address(self):
        return self.address

    # setter method
    def set_address(self, address):
        self.address = address


    def get_date(self):
        return self.date

    # setter method
    def set_date(self, date):
        self.date = date
