import pytest
from src.main import Category, Product


@pytest.fixture()
def product_1():
    return Product("продукт1", "описание продукта", 10000.0, 1)


@pytest.fixture()
def product_2():
    return Product("продукт2", "описание продукта", 10000.0, 1)


@pytest.fixture()
def category_initialization(product_1, product_2):
    return Category("Категория 1", "Описание категории", [product_1, product_2])


def test_category_init(category_initialization, product_1, product_2):
    assert category_initialization.name == "Категория 1"
    assert category_initialization.description == "Описание категории"
    assert category_initialization.products == [product_1, product_2]
    assert category_initialization.total_categories == 1
    assert category_initialization.total_unique_products == 2


@pytest.fixture()
def product_initialization():
    return Product("продукт1", "описание продукта", 10000.0, 1)


def test_product_init(product_initialization):
    assert product_initialization.name == "продукт1"
    assert product_initialization.description == "описание продукта"
    assert product_initialization.price == 10000.0
    assert product_initialization.quantity == 1
