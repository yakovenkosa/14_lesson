class Category:
    """Создание класса категории продуктов"""

    name: str
    description: str
    products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        """Метод инициализации экземпляров класса Category"""

        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(set([product.name for product in products]))


class Product:
    """Создание класса продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации экземпляров класса Product"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
