from crud import(
    create_category,
    create_supplier,
    create_product,
    get_all_categories,
    get_all_suppliers,
    create_stock_movement,
    get_all_products
                 )

from decimal import Decimal

def seed():
    electronics = create_category('Electronics')
    techtrade = create_supplier('TechTrade','7999999','pepasd@gmail.com',True,'2026-06-22T18:00:00')
    create_product(
            name = 'Iphone 99',
            sku = 1001,
            category_id = electronics.id,
            supplier_id = techtrade.id,
            purchase_price = Decimal('200.00'),
            selling_price = Decimal('300.00'),
            min_quantity = 10,
            is_active=True
        )
    create_stock_movement(
            product_id = get_all_products()[0].id,
            quantity = 20,
            movement_type = 'in',
            movement_date = '2026-01-01'
        )


seed()