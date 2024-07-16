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
        Category.all_quantity_unique_product += product.quantity
        if not isinstance(product, (Product, Smartphome, LawnGrass)):
            raise TypeError('Продукт не соответсвует классу')
        elif product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.__products.append(product)

    @property
    def products_list(self):
        product_info = []
        for product in self.__products:
            product_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return '\n'.join(product_info)

    def __len__(self):
        """Вывод количества продуктов на складе"""
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        """Добавление строкового отображения"""
        return f'Название категории: {self.name}, количество продуктов: {self.__len__()} шт.'