from typing import List
from models.product import Product
from models.discount import Discount

class CostCalculator:
    def __init__(self):
        self.items = []
        self.discounts = []
    
    def add_product(self, product: Product, quantity: int = 1):
        self.items.append({"product": product, "quantity": quantity})
    
    def add_discount(self, discount: Discount):
        self.discounts.append(discount)
    
    def calculate_subtotal(self):
        return sum(item["product"].get_price() * item["quantity"] for item in self.items)
    
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        total = subtotal
        
        for discount in self.discounts:
            total = discount.apply_discount(total)
        
        return total
    
    def get_summary(self):
        summary = {
            "items": [],
            "subtotal": self.calculate_subtotal(),
            "discounts": [discount.name for discount in self.discounts],
            "total": self.calculate_total()
        }
        
        for item in self.items:
            summary["items"].append({
                "product": str(item["product"]),
                "quantity": item["quantity"],
                "subtotal": item["product"].get_price() * item["quantity"]
            })
        
        return summary