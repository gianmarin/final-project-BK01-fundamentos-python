from data import WAREHOUSE, SHOPPING_CAR

#Función de Agregar Producto al Carrito de Compras
def add_product_to_shopping_car() -> None:
    code_product = input("Ingrese el código del producto: ").strip().upper()
    product_found = None
    for product in WAREHOUSE:
        if product["code"] == code_product:
            product_found = product
            break

    if not product_found:
        print("❌ Producto no encontrado en el catálogo.\n")
        return

    try:
        quantity = int(input("Ingrese la cantidad: "))
        if quantity <= 0:
            print("❌ La cantidad debe ser mayor a 0.\n")
            return
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número entero.\n")
        return

    # Buscar si ya está en el carrito
    for item in SHOPPING_CAR:
        if item["code"] == code_product:
            item["quantity"] += quantity
            print(f"✅ {quantity} unidades de {product_found['name']} agregadas al carrito.\n")
            return

    # Si no estaba en el carrito, agregar nuevo
    SHOPPING_CAR.append({
        "code": product_found["code"],
        "name": product_found["name"],
        "price": product_found["price"],
        "quantity": quantity
    })
    print(f"✅ {quantity} unidades de {product_found['name']} agregadas al carrito.\n")

def remove_product_from_shopping_car() -> None:
    code_product = input("Ingrese el código del producto a eliminar: ").strip().upper()
    for i, item in enumerate(SHOPPING_CAR):
        if item["code"] == code_product:
            del SHOPPING_CAR[i]
            print(f"✔ Producto {item['name']} eliminado del carrito.\n")
            return

    print("❌ El producto no está en el carrito.\n")

def empty_shopping_car() -> None:
    SHOPPING_CAR.clear()
    print("🧹 Carrito vaciado.\n")

def show_shopping_car() -> None:
    if not SHOPPING_CAR:
        print("🛒 El carrito está vacío.\n")
        return

    print("\n🛒 Contenido del carrito:")
    total = 0
    for item in SHOPPING_CAR:
        subtotal = item["price"] * item["quantity"]
        print(f"- {item['name']} (x{item['quantity']}) -> S/{subtotal:.2f}")
        total += subtotal
    print(f"Total: S/{total:.2f}\n")