from models.product import Product
from models.discount import Discount
from services.cost_calculator import CostCalculator

def test_cost_calculation():
    # Configuración
    calculator = CostCalculator()
    product1 = Product("Test Product 1", 100)
    product2 = Product("Test Product 2", 50)
    discount = Discount("Test Discount", 10)
    
    # Agregar productos y descuentos
    calculator.add_product(product1, 2)
    calculator.add_product(product2)
    calculator.add_discount(discount)
    
    # Verificaciones
    assert calculator.calculate_subtotal() == 250  # 2*100 + 50
    assert calculator.calculate_total() == 225    # 250 - 10%