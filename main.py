from product import Product, ProductRegistry


def main():
    print("=" * 50)
    print("Демонстрация паттерна Prototype (Прототип)")
    print("Пример: интернет-магазин товаров")
    print("=" * 50)
    print()
    
    # 1. Создаем реестр (хранилище шаблонов)
    registry = ProductRegistry()
    print("1. Создан реестр прототипов")
    print()
    
    # 2. Создаем примеры товаров (прототипы)
    shirt = Product("Футболка классическая", "Одежда", 999, "M", "Белый")
    laptop = Product("Ноутбук Work", "Электроника", 45000, "15.6 дюймов", "Серый")
    sneakers = Product("Кроссовки Sport", "Обувь", 3500, "42", "Черный")
    
    print("2. Созданы прототипы товаров:")
    shirt.show()
    laptop.show()
    sneakers.show()
    
    # 3. Регистрируем их в реестре
    registry.register("shirt", shirt)
    registry.register("laptop", laptop)
    registry.register("sneakers", sneakers)
    print()
    
    # 4. Создаем копии товаров из реестра
    print("3. Создаем копии товаров из реестра:")
    
    copy1 = registry.create_copy("shirt")
    if copy1:
        print("Копия футболки создана:")
        copy1.show()
    
    copy2 = registry.create_copy("laptop")
    if copy2:
        print("Копия ноутбука создана:")
        copy2.show()
    
    # 5. Демонстрируем независимость клонов
    print("=" * 50)
    print("4. Демонстрация независимости клонов")
    print("-" * 30)
    
    original = Product("Смартфон", "Электроника", 30000, "6.5 дюймов", "Золотой")
    clone = original.clone()
    
    print("Оригинал:", original.name, "-", original.price, "руб")
    print("Клон:    ", clone.name, "-", clone.price, "руб")
    
    # Изменяем клон
    clone.name = "Смартфон Pro"
    clone.price = 40000
    clone.color = "Черный"
    
    print()
    print("После изменения клона:")
    print("Оригинал:", original.name, "-", original.price, "руб", "-", original.color)
    print("Клон:    ", clone.name, "-", clone.price, "руб", "-", clone.color)
    print()
    print("✅ Оригинал не изменился!")
    
    print("=" * 50)
    print("Демонстрация завершена")


if name == "main":
    main()
