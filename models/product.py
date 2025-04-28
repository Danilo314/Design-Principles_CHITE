class Product:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
    
    def get_price(self):
        return self.base_price
    
    def __str__(self):
        return f"{self.name} (${self.base_price:.2f})"