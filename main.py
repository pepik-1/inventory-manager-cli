from datetime import date
from database import Base, engine
from crud import (
    create_category,
    create_product,
    create_stock_movement,
    create_supplier,
    deactivate_product,
    deactivate_supplier,
    get_all_categories,
    get_all_products,
    get_all_stock_movements,
    get_all_suppliers,
    get_current_stock_by_product,
    get_low_stock_products,
    get_potential_profit,
    get_product_by_id,
    get_products_by_category,
    get_products_by_supplier,
    get_total_purchase_value,
    get_total_selling_value,
    update_product_prices,
)

def main():
    # Создаем таблицы в базе данных, если их еще нет
    Base.metadata.create_all(engine)

    while True:
        print('\n=== МЕНЕДЖЕР ИНВЕНТАРЯ CLI ===')
        print('1. Создать категорию')
        print('2. Показать все категории')
        print('3. Создать поставщика')
        print('4. Показать всех поставщиков')
        print('5. Деактивировать поставщика')
        print('6. Создать товар')
        print('7. Показать все товары')
        print('8. Показать товар по id')
        print('9. Обновить цену товара')
        print('10. Деактивировать товар')
        print('11. Добавить поступление товара (IN)')
        print('12. Добавить списание товара (OUT)')
        print('13. Добавить корректировку остатка (ADJUSTMENT)')
        print('14. Показать историю операций')
        print('15. Показать операции по конкретному товару')
        print('16. Показать текущие остатки')
        print('17. Показать товары, которые заканчиваются')
        print('18. Показать финансовую стоимость склада')
        print('19. Показать товары конкретной категории')
        print('20. Показать товары конкретного поставщика')
        print('0. Выход')
        
        try:
            user_choice = int(input('\nВыберите пункт меню: '))
        except ValueError:
            print('Ошибка: Введите число!')
            continue

        if user_choice == 1:
            user_cat = input('Введите название новой категории: ')
            cat = create_category(user_cat)
            if cat:
                print(f'Категория "{cat.name}" успешно создана с ID: {cat.id}')
            else:
                print('Не удалось создать категорию (возможно, имя уже занято).')

        elif user_choice == 2:
            print('\n--- СПИСОК КАТЕГОРИЙ ---')
            for category in get_all_categories():
                print(f'ID: {category.id} | Название: {category.name}')
        
        elif user_choice == 3:
            name = input('Имя поставщика: ')
            phone = input('Телефон: ')
            email = input('Email: ')
            is_active_input = input('Активен? (Yes/No): ').strip().lower()
            is_active = True if is_active_input == 'yes' else False
            
            date_str = input('Введите дату создания (ГГГГ-ММ-СС): ')
            try:
                date_created = date.fromisoformat(date_str)
                sup = create_supplier(name, phone, email, is_active, date_created)
                if sup:
                    print(f'Поставщик успешно создан с ID: {sup.id}')
                else:
                    print('Ошибка при создании поставщика.')
            except ValueError:
                print('Неверный формат даты! Используйте ГГГГ-ММ-СС (например, 2026-06-27).')

        elif user_choice == 4:
            print('\n--- СПИСОК ПОСТАВЩИКОВ ---')
            for supplier in get_all_suppliers():
                print(f'ID: {supplier.id} | Имя: {supplier.name} | Активен: {supplier.is_active}')

        elif user_choice == 5:
            supplier_id = int(input('Введите ID поставщика для деактивации: '))
            deactivate_supplier(supplier_id)
            print('Статус изменен.')
        
        elif user_choice == 6:
            name = input('Название товара: ')
            sku = int(input('Артикул (SKU): '))
            category_id = int(input('ID категории: '))
            supplier_id = int(input('ID поставщика: '))
            purchase_price = float(input('Закупочная цена: ')) # Заменили Decimal на float
            selling_price = float(input('Цена продажи: '))     # Заменили Decimal на float
            min_quantity = int(input('Минимальный остаток: '))
            
            is_active_input = input('Активен? (Yes/No): ').strip().lower()
            is_active = True if is_active_input == 'yes' else False
            
            # Убрали ручной ввод даты для товара, crud.py ставит сегодняшнюю сам
            prod = create_product(name, sku, category_id, supplier_id, purchase_price, selling_price, min_quantity, is_active)
            if prod:
                print(f'Товар успешно создан с ID: {prod.id}')
            else:
                print('Ошибка при создании товара (проверьте ID категории/поставщика или SKU).')

        elif user_choice == 7:
            print('\n--- СПИСОК ТОВАРОВ ---')
            for product in get_all_products():
                print(f'ID: {product.id} | {product.name} | SKU: {product.sku} | Цена: {product.selling_price} | Активен: {product.is_active}')

        elif user_choice == 8:
            product_id = int(input('Введите ID товара: '))
            product = get_product_by_id(product_id)
            if product:
                print(f'Товар: {product.name}\nSKU: {product.sku}\nКатегория: {product.category.name if product.category else "Нет"}\nПоставщик: {product.supplier.name if product.supplier else "Нет"}')
            else:
                print('Товар не найден.')
        
        elif user_choice == 9:
            product_id = int(input('Введите ID товара: '))
            new_purchase_price = float(input('Новая закупочная цена: '))
            new_selling_price = float(input('Новая цена продажи: '))
            update_product_prices(product_id, new_purchase_price, new_selling_price)
            print('Цены успешно обновлены.')

        elif user_choice == 10:
            product_id = int(input('Введите ID товара для деактивации: '))
            deactivate_product(product_id)
            print('Товар деактивирован.')

        elif user_choice == 11:
            product_id = int(input('Введите ID товара: '))
            quantity = int(input('Количество для поступления: '))
            # Убрали ввод даты
            create_stock_movement(product_id, quantity, 'in')
            print('Поступление успешно оформлено.')

        elif user_choice == 12:
            product_id = int(input('Введите ID товара: '))
            quantity = int(input('Количество для списания: '))
            create_stock_movement(product_id, quantity, 'out')
            print('Списание успешно оформлено.')

        elif user_choice == 13:
            product_id = int(input('Введите ID товара: '))
            quantity = int(input('Количество для корректировки: '))
            create_stock_movement(product_id, quantity, 'adjustment')
            print('Корректировка успешно оформлена.')

        elif user_choice == 14:
            print('\n--- ИСТОРИЯ ВСЕХ ОПЕРАЦИЙ ---')
            for m in get_all_stock_movements():
                # Исправлены имена полей на movement_type и created_at
                print(f'ID операции: {m.id} | ID товара: {m.product_id} | Кол-во: {m.quantity} | Тип: {m.movement_type} | Дата: {m.created_at}')

        elif user_choice == 15:
            product_id = int(input('Введите ID товара: '))
            print(f'\n--- ИСТОРИЯ ПО ТОВАРУ ID {product_id} ---')
            for m in get_movements_by_product(product_id):
                # Исправлены имена полей на movement_type и created_at
                print(f'ID операции: {m.id} | Кол-во: {m.quantity} | Тип: {m.movement_type} | Дата: {m.created_at}')

        elif user_choice == 16:
            print('\n--- ТЕКУЩИЕ ОСТАТКИ НА СКЛАДЕ ---')
            for row in get_current_stock_by_product():
                print(f'Товар: {row.product_name} | Остаток: {row.current_stock}')

        elif user_choice == 17:
            print('\n--- КРИТИЧЕСКИЙ УРОВЕНЬ ОСТАТКОВ ---')
            for row in get_low_stock_products():
                print(f'Товар: {row.product_name} | Текущий остаток: {row.current_stock} (Минимум: {row.min_quantity})')

        elif user_choice == 18:
            print('\n--- ФИНАНСОВЫЙ ОТЧЕТ СКЛАДА ---')
            print(f'Общая стоимость по закупочным ценам: {get_total_purchase_value()}')
            print(f'Общая стоимость по ценам продажи: {get_total_selling_value()}')
            print(f'Потенциальная прибыль: {get_potential_profit()}')

        elif user_choice == 19:
            cat_id = int(input('Введите ID интересующей категории: '))
            print(f'\n--- ТОВАРЫ В КАТЕГОРИИ ID {cat_id} ---')
            for product in get_products_by_category(cat_id): # Добавлен аргумент cat_id
                print(f'ID: {product.id} | Название: {product.name}')

        elif user_choice == 20:
            sup_id = int(input('Введите ID интересующего поставщика: '))
            print(f'\n--- ТОВАРЫ ОТ ПОСТАВЩИКА ID {sup_id} ---')
            for product in get_products_by_supplier(sup_id): # Добавлен аргумент sup_id
                print(f'ID: {product.id} | Название: {product.name}')

        elif user_choice == 0:
            print('Выход из программы. Пока!')
            break

if __name__ == "__main__":
    main()