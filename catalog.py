from data import WAREHOUSE

# Función de Mostrar Detalle de Catálogo
def show_catalog() -> None:
    print("\n📋 Catálogo de Productos:")
    print("Código | Producto           | Precio")
    print("------------------------------------------")
    for product in WAREHOUSE:
        print(f"{product['code']} | {product["name"]}{" "*(20-len(product["name"]))} | S/{product['price']:.2f}")
    print()