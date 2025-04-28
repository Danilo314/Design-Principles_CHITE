from models.product import Product
from models.discount import Discount
from services.cost_calculator import CostCalculator
from services.invoice_generator import InvoiceGenerator

def main():
    # Crear productos
    laptop = Product("Laptop Gamer", 1200)
    mouse = Product("Mouse Inalámbrico", 50)
    keyboard = Product("Teclado Mecánico", 150)
    
    # Crear descuentos
    black_friday = Discount("Black Friday", 15)
    loyalty = Discount("Descuento por fidelidad", 5)
    
    # Configurar calculadora
    calculator = CostCalculator()
    calculator.add_product(laptop)
    calculator.add_product(mouse, 2)
    calculator.add_product(keyboard)
    calculator.add_discount(black_friday)
    calculator.add_discount(loyalty)
    
    # Calcular y mostrar resultados
    summary = calculator.get_summary()
    invoice = InvoiceGenerator.generate_invoice(summary)
    
    print(invoice)

if __name__ == "__main__":
    main()