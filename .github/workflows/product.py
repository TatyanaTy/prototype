from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    """Абстрактный класс прототипа - основа паттерна"""
    
    @abstractmethod
    def clone(self):
        """Метод клонирования"""
        pass
    
    @abstractmethod
    def show(self):
        """Метод отображения информации"""
        pass


class Product(Prototype):
    """Класс товара - конкретная реализация прототипа"""
    
    def init(self, name, category="Без категории", price=0.0, size="Стандартный", color="Белый"):
        self.name = name           # Название товара
        self.category = category   # Категория товара
        self.price = price         # Цена
        self.size = size           # Размер
        self.color = color         # Цвет
    
    def clone(self):
        """Создает точную копию товара"""
        return copy.deepcopy(self)  # deepcopy - полностью копирует все данные
    
    def show(self):
        """Выводит информацию о товаре"""
        print("Товар:", self.name)
        print("  Категория:", self.category)
        print("  Цена:", self.price, "руб")
        print("  Размер:", self.size)
        print("  Цвет:", self.color)
        print("---")


class ProductRegistry:
    """Реестр прототипов - хранит шаблоны товаров"""
    
    def init(self):
        self.prototypes = {}  # Словарь для хранения прототипов
    
    def register(self, key, prototype):
        """Сохраняет прототип под ключом"""
        self.prototypes[key] = prototype
        print(f"Зарегистрирован прототип с ключом: {key}")
    
    def create_copy(self, key):
        """Создает копию из реестра по ключу"""
        if key in self.prototypes:
            print(f"Клонируем прототип с ключом: {key}")
            return self.prototypes[key].clone()
        else:
            print(f"Ошибка: прототип '{key}' не найден")
            return None
