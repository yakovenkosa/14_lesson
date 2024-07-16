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

    @price.deleter
    def price(self):
        """Делитер для атрибута цены"""
        print(f"Удаление цены для продукта '{self.name}'")
        del self._price

    def __str__(self):
        """Добавление строкового отображения"""
        return f'\nНазвание продукта: {self.name}, Цена: {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Метод сложения объектов (сложением сумм, умноженных на количество на складе)."""
        if self.__class__.__name__ == other.__class__.__name__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


class Smartphome(Product):
    """Создание класса Smartphome (базовый класс Product)"""

    efficiency: float
    model: str
    memory: int
    colour: int

    def __init__(self, name, description, price, quantity, efficiency, model, memory, colour):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.colour = colour

    def __str__(self):
        """Добавление строкового отображения класса SmartPhones"""
        return f'\nПроизводительность: {self.efficiency}, модель: {self.model}.\nОбъем памяти: {self.memory} ГБ. Цвет: {self.color}'

    def __add__(self, other):
        """Функция суммирует объекты только одного класса, в случае, если объект другого класса - выводится ошибки"""
        if isinstance(other, Smartphome):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise ValueError("Товары из разных классов продуктов")

class LawnGrass(Product):
    """Создание класса LawnGrass (базовый класс Product)"""

    country: str
    period: int
    colour: int

    def __init__(self, name, description, price, quantity, country, period, colour):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.colour = colour

    def __str__(self):
        """Добавление строкового отображения класса LawnGrass"""
        return f'\nСтрана-производитель: {self.country}, срок прорастания: {self.period}, цвет: {self.colour}'

    def __add__(self, other):
        """Функция суммирует объекты только одного класса, в случае, если объект другого класса - выводится ошибки"""
        if isinstance(other, LawnGrass):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise ValueError("Товары из разных классов продуктов")
