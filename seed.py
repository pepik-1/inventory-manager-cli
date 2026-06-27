from datetime import date
from database import SessionLocal
from models import Category, Supplier
from sqlalchemy import select
from crud import (
    create_category,
    create_supplier,
    create_product,
    create_stock_movement
)

def seed():
    with SessionLocal() as session:
        stmt_cat = select(Category).where(Category.name == 'Electronics')
        electronics = session.execute(stmt_cat).scalar_one_or_none()
        
        if not electronics:
            print("Категория 'Electronics' не найдена, создаем...")
            electronics = create_category('Electronics')
        else:
            print("Категория 'Electronics' уже существует, используем её.")

        stmt_sup = select(Supplier).where(Supplier.name == 'TechTrade')
        techtrade = session.execute(stmt_sup).scalar_one_or_none()
        
        if not techtrade:
            print("Поставщик 'TechTrade' не найден, создаем...")
            techtrade = create_supplier(
                name='TechTrade', 
                phone='7999999', 
                email='pepasd@gmail.com', 
                is_active=True, 
                date_created=date(2026, 6, 22)
            )
        else:
            print("Поставщик 'TechTrade' уже существует, используем его.")



    if electronics and techtrade:
        iphone = create_product(
            name='Iphone 99',
            sku=1001,
            category_id=electronics.id,
            supplier_id=techtrade.id,
            purchase_price=200.00,
            selling_price=300.00,
            min_quantity=10,
            is_active=True
        )
        
        if iphone:
            print("Продукт 'Iphone 99' успешно создан!")
            create_stock_movement(
                product_id=iphone.id,
                quantity=20,
                movement_type='in'
            )
            print("Движение товара добавлено!")
        else:
            print("Продукт 'Iphone 99' (SKU 1001) уже есть в базе, пропускаем создание.")



if __name__ == "__main__":
    seed()