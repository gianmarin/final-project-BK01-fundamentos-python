from typing import List, Dict

# Inicialización de Data de Catálogo de productos
WAREHOUSE: List[Dict[str, str | float]] = [
    {
        "code": "A001", 
        "name": "Pan", 
        "price": 1.50
    },
    {   "code": "A002", 
        "name": "Leche", 
        "price": 4.00
    }
]

# Inicialización de Data de Carrito de Compras
SHOPPING_CAR: List[Dict[str, str | float | int]] = []