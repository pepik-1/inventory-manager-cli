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

    if not get_all_categories():
        create_category('Electronics')
        create_category('Clothing')
        create_category('Books')    
    
    if not get_all_suppliers():
        create_supplier(
            name = 'Supplies Inc.',
            phone = '+7234567890',
            email = 'pepe@gffea.com'
        )
    
    if not get_all_products():
         create_product(
            name = 'Iphone 99',
            sku = 1001,
            category_id = get_all_categories()[0].id,
            supplier_id = get_all_suppliers()[0].id,
            purchase_price = Decimal('200.00'),
            selling_price = Decimal('300.00'),
            min_quantity = 10
        )

         create_product(
            name = 't-shirt',
            sku = 1002,
            category_id = get_all_categories()[1].id,
            supplier_id = get_all_suppliers()[0].id,
            purchase_price = Decimal('10.00'),
            selling_price = Decimal('20.00'),
            min_quantity = 50
        )

         create_product(
            name = 'smt book',
            sku = 1003,
            category_id = get_all_categories()[2].id,
            supplier_id = get_all_suppliers()[0].id,
            purchase_price = Decimal('5.00'),
            selling_price = Decimal('15.00'),
            min_quantity = 30
        )
    
    if not get_all_stock_movements():
        create_stock_movement(
            product_id = get_all_products()[0].id,
            quantity = 20,
            movement_type = 'in',
            movement_date = '2026-01-01'
        )

        create_stock_movement(
            product_id = get_all_products()[1].id,
            quantity = 100,
            movement_type = 'in',
            movement_date = '2026-01-02'
        )

        create_stock_movement(
            product_id = get_all_products()[2].id,
            quantity = 50,
            movement_type = 'in',
            movement_date = '2026-01-03'
        )
    
    


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