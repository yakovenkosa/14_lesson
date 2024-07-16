from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """Абстрактный класс c выделеным общим функционалом"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class MixinLog:
    """Миксин, который можно добавить к каждому классу для вывода информации в консоль о том, что был создан объект."""
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"Создание нового экземпляра продукта - {self.__class__.__name__} ({self.__dict__.items()})"

class Product(AbstractProduct, MixinLog):
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

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__price}, {self.quantity}'
        super().__repr__()

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
    colour: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, colour):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.colour = colour

    def __str__(self):
        """Добавление строкового отображения класса SmartPhones"""
        return f'\nПроизводительность: {self.efficiency}, модель: {self.model}.\nОбъем памяти: {self.memory} ГБ. Цвет: {self.colour}'

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


# работа с категориями и продуктами
product_1 = Product('Redmi', 'smth', 40_000, 5)  # Экземпляр класса Product
product_2 = Product('Nokia', 'smth', 50_000, 10)  # Экземпляр класса Product
print(f'\nМетод add для 2х экземпляров класса {Product.__add__(product_1, product_2)}:')

phone_1 = Smartphome('Xiaomi', 'smartphone', 45000, 3, 1500.00, 'V50',
                          512, 'Silver')
phone_2 = Smartphome('Motorola', 'Slider', 5000, 3, 500, 'V3',
                          4, 'Black')

print(phone_1)

print(f'Общая сумма категории "Смартфон": {phone_1 + phone_2}')

grass_1 = LawnGrass('Примгазон', 'Премиум', 3000, 5, 'Россия',
                        15, 'green')

grass_2 = LawnGrass('Газон дача', 'Эконом', 1500, 10, 'Россия',
                        10, 'green')

print(grass_1)

print(f'Общая сумма категории "Трава газонная": {grass_1 + grass_2}')