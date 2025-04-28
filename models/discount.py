class Discount:
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage
    
    def apply_discount(self, amount):
        return amount * (1 - self.percentage / 100)