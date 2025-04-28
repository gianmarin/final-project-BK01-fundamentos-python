from typing import List
import datetime
from data import SHOPPING_CAR

# Función de Pago
def checkout() -> None:
    if not SHOPPING_CAR:
        print("🛒 No hay productos en el carrito para finalizar la compra.\n")
        return

    print("\n🧾 Resumen de compra:")
    total = 0
    resumen = []
    for item in SHOPPING_CAR:
        subtotal = item["price"] * item["quantity"]
        print(f"- {item['name']} (x{item['quantity']}) -> S/{subtotal:.2f}")
        resumen.append(f"{item['name']} (x{item['quantity']}) -> S/{subtotal:.2f}")
        total += subtotal
    print(f"Total a pagar: S/{total:.2f}\n")

    print("💳 Procesando pago...")
    print("✅ Pago realizado. ¡Gracias por tu compra!\n")

    save_purchase_history(resumen, total)
    SHOPPING_CAR.clear()

# Función de Guardar Historial de Pago
def save_purchase_history(products: List[str], total: float) -> None:
    try:
        now = datetime.datetime.now()
        fecha = now.strftime("%d/%m/%y %H:%M:%S") + f":{int(now.microsecond / 1000):03d}"

        with open("logs_checkout.txt", "a", encoding="utf-8") as file:
            file.write(f"Fecha: {fecha}\n")
            for line in products:
                file.write(f"{line}\n")
            file.write(f"Total: S/{total:.2f}\n")
            file.write("-" * 30 + "\n")
    except Exception as e:
        print(f"⚠️ Error al guardar historial: {e}")