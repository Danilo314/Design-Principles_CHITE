class InvoiceGenerator:
    @staticmethod
    def generate_invoice(summary):
        invoice = "=== FACTURA ===\n"
        invoice += "\nProductos:\n"
        
        for item in summary["items"]:
            invoice += f"- {item['product']} x {item['quantity']}: ${item['subtotal']:.2f}\n"
        
        invoice += f"\nSubtotal: ${summary['subtotal']:.2f}\n"
        
        if summary["discounts"]:
            invoice += f"Descuentos aplicados: {', '.join(summary['discounts'])}\n"
        
        invoice += f"\nTOTAL A PAGAR: ${summary['total']:.2f}\n"
        invoice += "================="
        
        return invoice