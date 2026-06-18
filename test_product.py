import pytest
from product import Product, ProductRegistry


def test_clone_creates_new_object():
    """ТЕСТ 1: Проверяем, что клон - это новый объект"""
    # Создаем оригинальный товар
    original = Product("Футболка", "Одежда", 999, "M", "Черный")
    
    # Клонируем его
    cloned = original.clone()
    
    # Проверяем, что это разные объекты (разные адреса в памяти)
    assert original is not cloned, "Клон и оригинал - один объект!"
    
    # Проверяем, что данные совпадают
    assert original.name == cloned.name, "Имена не совпадают"
    assert original.price == cloned.price, "Цены не совпадают"


def test_clone_independent_from_original():
    """ТЕСТ 2: Изменения в клоне не влияют на оригинал"""
    original = Product("Ноутбук", "Электроника", 1500, "15 дюймов", "Серый")
    cloned = original.clone()
    
    # Изменяем данные в клоне
    cloned.name = "Ноутбук Pro"
    cloned.price = 2000
    
    # Проверяем, что оригинал остался прежним
    assert original.name == "Ноутбук", "Оригинал изменился!"
    assert original.price == 1500, "Цена оригинала изменилась!"
    assert cloned.name == "Ноутбук Pro", "Клон не изменился!"
    assert cloned.price == 2000, "Цена клона не изменилась!"


def test_registry_works():
    """ТЕСТ 3: Проверяем работу реестра прототипов"""
    # Создаем реестр
    registry = ProductRegistry()
    
    # Создаем прототип
    prototype = Product("Кроссовки", "Обувь", 4500, "42", "Белый")
    
    # Регистрируем его
    registry.register("sneakers", prototype)
    
    # Создаем копию из реестра
    copied = registry.create_copy("sneakers")
    
    # Проверяем, что копия создалась
    assert copied is not None, "Копия не создалась!"
    assert copied is not prototype, "Вернулся оригинал, а не копия!"
    assert copied.name == "Кроссовки", "Имя не совпадает"
    assert copied.price == 4500, "Цена не совпадает"


def test_registry_not_found():
    """ТЕСТ 4: Проверяем обработку ошибки - прототип не найден"""
    registry = ProductRegistry()
    
    # Пытаемся создать копию несуществующего прототипа
    result = registry.create_copy("nonexistent")
    
    # Должен вернуться None (ничего)
    assert result is None, "Должна быть ошибка!"


def test_clone_preserves_all_attributes():
    """ТЕСТ 5: Все атрибуты копируются правильно"""
    original = Product("Телефон", "Электроника", 50000, "6.7 дюймов", "Синий")
    cloned = original.clone()
    
    # Проверяем каждый атрибут
    assert cloned.name == original.name, "Имя"
    assert cloned.category == original.category, "Категория"
    assert cloned.price == original.price, "Цена"
    assert cloned.size == original.size, "Размер"
    assert cloned.color == original.color, "Цвет"


