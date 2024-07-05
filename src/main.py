class Category:
    """Создание класса категории продуктов"""

    name: str
    description: str
    products: list

    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        """Метод инициализации экземпляров класса Category"""

        self.__name = name
        self.__description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_unique_products += len(set([product.name for product in products]))

    def add_product(self, product):
        """Метод для добавления продукта в список продуктов категории"""
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def products_list(self):
        product_info = []
        for product in self.__products:
            product_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return '\n'.join(product_info)

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

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """Метод для создания нового товара"""
        return cls(name, description, price, quantity)

    def add_new_product(self, products):
        """Создает товар и возвращает объект, который можно добавлять в список товаров"""
        for product in products:
            if product.name.lower() == self.name.lower():
                product.quantity += self.quantity
                product.price = max(product.price, self.price)
                return product
        return self

    @property
    def price(self):
        """Геттер для атрибута цены"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер для атрибута цены"""
        if new_price <= 0:
            print("Цена введена некорректно.")
        else:
            self._price = new_price
