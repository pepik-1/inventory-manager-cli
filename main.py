from decimal import Decimal

from database import Base,engine

from crud import(

    create_category,
    create_product,
    create_stock_movement,
    create_supplier,
    deactivate_product,
    deactivate_supplier,
    delete_category,
    delete_product,
    delete_stock_movement,
    delete_supplier,
    get_all_categories,
    get_all_products,
    get_all_stock_movements,
    get_all_suppliers,
    get_category_by_id,
    get_current_stock_by_product,
    get_low_stock_products,
    get_movements_by_product,
    get_movements_with_product,
    get_potential_profit,
    get_product_by_id,
    get_products_by_category,
    get_products_by_supplier,
    get_products_count_by_category,
    get_products_count_by_supplier,
    get_products_with_category_and_supplier,
    get_supplier_by_id,
    get_total_purchase_value,
    get_total_selling_value,
    update_category_name,
    update_product_min_quantity,
    update_product_prices,
    update_supplier_contacts,
    get_all_categories,       
    get_category_by_id,
    update_category_name,
    delete_category,
    create_supplier,
    get_all_suppliers,
    get_supplier_by_id,
    update_supplier_contacts,
    deactivate_supplier,
    delete_supplier,
    create_product,
    get_all_products,
    get_product_by_id,
    get_products_by_category,
    get_products_by_supplier,
    update_product_prices,
    update_product_min_quantity,
    deactivate_product,
    delete_product,
    create_stock_movement,
    get_all_stock_movements,
    get_movements_by_product,
    delete_stock_movement,
    get_products_with_category_and_supplier,
    get_movements_with_product,
    get_products_count_by_category,
    get_products_count_by_supplier,
    get_current_stock_by_product,
    get_low_stock_products,
    get_total_purchase_value,
    get_total_selling_value,
    get_potential_profit,
)

def main():
    Base.metadata.create_all(engine)


    while True:

        print('1. Создать категорию')
        print('2. Показать все категории')
        print('3. Создать поставщика')
        print('4. Показать всех поставщиков')
        print('5. Деактивировать поставщика')
        print(' 6. Создать товар')
        print(' 7. Показать все товары')
        print('8. Показать товар по id')
        print('9. Обновить цену товара')
        print('10. Деактивировать товар')
        print('11. Добавить поступление товара')
        print('12. Добавить списание товара')
        print('13. Добавить корректировку остатка')
        print('14. Показать историю операций')
        print('15. Показать операции по товару')
        print('16. Показать текущие остатки')
        print('17. Показать товары, которые заканчиваются')
        print('18. Показать общую стоимость склада')
        print('19. Показать товары по категориям')
        print('20. Показать товары по поставщикам')
        user_choice = int(input())


        if user_choice == 1:
            user_cat = input('enter a name of a new category')
            create_category(user_cat)

        if user_choice == 2:
            get_all_categories()
        
        if user_choice == 3:
            name = input('name')
            num = input('number')
            email = input('email')
            is_active = input('Yes/No')
            if is_active == 'Yes':
                is_active = True
            elif is_active=='No':
                is_active = False
            create_supplier(name,num,email,is_active)






    








    it = create_department('IT')
    hr = create_department('HR')

    if it:
        ivan = create_employee(
            name = 'Ivan',
            salary = Decimal('120000.00'),
            department_id = it.id
        )

        anna = create_employee(
            name = 'Anna',
            salary = Decimal('125000.00'),
            department_id = it.id
        )

        if ivan:
            create_project(
                name = 'Internal CRM',
                budget = Decimal('50000.00'),
                employee_id = ivan.id
            )
    
        if anna:
            create_project(
                name ='Mobile CRM',
                budget = Decimal('100000.00'),
                employee_id = anna.id
            )

        print('all departaments:')
        for department in get_all_departments():
            print(department.id, department.name)

        print('all employees:')
        for employee in get_all_employees():
            print(employee.id, employee.name)

        print('all projects:')
        for project in get_all_projects():
            print(project.id, project.name)

        print('employees and departments:')
        for employee_name,department_name in get_employees_with_department_names():
            print(employee_name, department_name)

        print('projects,employees,departments:')
        for row in get_projects_employees_departments():
            print(
                row.project_name,
                row.employee_name,
                row.department_name
            )

main()     