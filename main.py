from catalog import show_catalog
from cart import (
    add_product_to_shopping_car,
    remove_product_from_shopping_car,
    empty_shopping_car,
    show_shopping_car
)
from checkout import checkout

# Función de Mostrar Menu
def show_menu() -> None:
    print("""
    1. Ver catálogo
    2. Agregar producto al carrito
    3. Eliminar producto del carrito
    4. Vaciar carrito
    5. Mostrar carrito
    6. Finalizar compra
    7. Salir
    """)

# Función de Menu Principal
def main() -> None:
    while True:
        show_menu()
        try:
            option = int(input("> Escoja opción: "))
        except ValueError:
            print("🚩 Entrada inválida. Por favor, elige un número del menú.\n")
            continue

        if option == 1:
            show_catalog()
        elif option == 2:
            add_product_to_shopping_car()
        elif option == 3:
            remove_product_from_shopping_car()
        elif option == 4:
            empty_shopping_car()
        elif option == 5:
            show_shopping_car()
        elif option == 6:
            checkout()
        elif option == 7:
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("🚩 Opción no válida. Elige un número del 1 al 7.\n")

# Ejecutar
if __name__ == "__main__":
    main()
