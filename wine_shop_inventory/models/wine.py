class Wine:
    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, producer_id, id=None):
        self.name = name 
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.producer_id = producer_id
        self.id = id

    def get_markup(self):
        return ((self.selling_price - self.buying_cost) / self.buying_cost) * 100


