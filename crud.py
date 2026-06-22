from decimal import Decimal

from sqlalchemy import case, delete, func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from database import SessionLocal
from models import Product,Stock_movement,Supplier,Category
from datetime import date
from typing import Optional

def create_category(name:str):
    with SessionLocal() as session:
        try:
            category = Category(name=name)
            session.add(category)
            session.commit()
            session.refresh(category)
            return category
        except IntegrityError:
            session.rollback()
            return None

def get_all_categories():
    with SessionLocal() as session:
        stmt = select(Category)
        return session.execute(stmt).scalars().all()

def get_category_by_id(cat_id:int):
    with SessionLocal() as session:
        cat = session.get(Employee, cat_id)

        stmt = select(Category).options(joinedload(Category.products)).where(Category.id == cat_id)

        return session.execute(stmt).scalar_one_or_none()

def update_category_name(name:str):
    with SessionLocal() as session:
        category = session.get(Category, category_id)

        if category is None:
            return None

        category.name = new_category_name
        session.commit()
        session.refresh(category)

        return category

def delete_category(cat_id:int):
    with SessionLocal() as session:
        category = session.get(Category, category_id)

        if category is None:
            return False

        session.delete(category)
        session.commit()

        return True


def create_supplier(name:str,phone:str,email:str,is_active:bool,created_at:str):
    with SessionLocal() as session:
        try:
            supplier = Supplier(
                name=name,
                phone = phone,
                email = email,
                is_active = is_active,
                created_at = created_at
            
            )
            session.add(supplier)
            session.commit()
            session.refresh(supplier)
            return supplier
        except IntegrityError:
            session.rollback()
            return None

def get_all_suppliers():
    with SessionLocal() as session:
        stmt = select(Supplier)
        return session.execute(stmt).scalars().all()

def get_supplier_by_id(sup_id:int) -> Supplier|None:
    with SessionLocal() as session:
        sup = session.get(Supplier, sup_id)

        stmt = select(Supplier).options(joinedload(Supplier.products)).where(Supplier.id == sup_id)

        return session.execute(stmt).scalar_one_or_none()

def update_supplier_contacts(sup_id:int, new_name:str) -> Supplier|None:
    with SessionLocal() as session:
        supplier = session.get(Supplier, sup_id)

        if supplier is None:
            return None

        supplier.name = new_name
        session.commit()
        session.refresh(supplier)

        return supplier

def deactivate_supplier(sup_id:int) -> Supplier|None:
    with SessionLocal() as session:
        supplier = session.get(Supplier, sup_id)

        if supplier is None:
            return None

        supplier.is_active = False
        session.commit()
        session.refresh(supplier)

        return supplier

def delete_supplier(sup_id:int) :
    with SessionLocal() as session:
        supplier = session.get(Supplier, sup_id)

        if supplier is None:
            return False

        session.delete(supplier)
        session.commit()

        return True


def create_product(name: str, sku:int,category_id:int,supplier_id:int,purchase_price:int,selling_price:int,min_quantity:int,is_active:bool):
    with SessionLocal() as session:
        try:
            product = Product(
                name=name,
                sku = sku,
                category_id=category_id,
                supplier_id=supplier_id,
                purchase_price=purchase_price,
                selling_price = selling_price,
                min_quantity = min_quantity
                              )
            session.add(product)
            session.commit()
            session.refresh(product)
            return product
        except IntegrityError:
            session.rollback()
            return None

def get_all_products():
    with SessionLocal() as session:
        stmt = select(Product)
        return session.execute(stmt).scalars().all()
    
def get_product_by_id(prod_id:int):
    with SessionLocal() as session:
        prod = session.get(Product, prod_id)

        stmt = select(Product).options(joinedload(Product.category), joinedload(Product.supplier)).where(Product.id == prod_id)

        return session.execute(stmt).scalar_one_or_none()
    
def get_products_by_category(cat_id:int):
    with SessionLocal() as session:
        stmt = select(Product).where(Product.category_id == cat_id)
        return session.execute(stmt).scalars().all()

def get_products_by_supplier(sup_id:int):
    with SessionLocal() as session:
        stmt = select(Product).where(Product.supplier_id == sup_id)
        return session.execute(stmt).scalars().all()
    
def update_product_prices(prod_id:int, new_purchase_price:float, new_selling_price:float):
    with SessionLocal() as session:
        product = session.get(Product, prod_id)

        if product is None:
            return None

        product.purchase_price = new_purchase_price
        product.selling_price = new_selling_price
        session.commit()
        session.refresh(product)

        return product
    
def update_product_min_quantity(prod_id:int, new_min_quantity:int):
    with SessionLocal() as session:
        product = session.get(Product, prod_id)

        if product is None:
            return None

        product.min_quantity = new_min_quantity
        session.commit()
        session.refresh(product)

        return product

def deactivate_product(prod_id:int):
    with SessionLocal() as session:
        product = session.get(Product, prod_id)

        if product is None:
            return None

        product.is_active = False
        session.commit()
        session.refresh(product)

        return product 
    
def delete_product(prod_id:int):
    with SessionLocal() as session:
        product = session.get(Product, prod_id)

        if product is None:
            return False

        session.delete(product)
        session.commit()

        return True
    
def create_stock_movement(product_id:int, quantity:int, movement_type:str,comment:Optional[str]):
    with SessionLocal() as session:
        try:
            stock_movement = Stock_movement(
                product_id=product_id,
                quantity=quantity,
                movement_type=movement_type,
                comment = comment
            )
            session.add(stock_movement)
            session.commit()
            session.refresh(stock_movement)
            return stock_movement
        except IntegrityError:
            session.rollback()
            return None
        
def get_all_stock_movements():
    with SessionLocal() as session:
        stmt = select(Stock_movement)
        return session.execute(stmt).scalars().all()
    
def get_movements_by_product(prod_id:int):
    with SessionLocal() as session:
        stmt = select(Stock_movement).where(Stock_movement.product_id == prod_id)
        return session.execute(stmt).scalars().all()
    
def delete_stock_movement(movement_id:int):
    with SessionLocal() as session:
        movement = session.get(Stock_movement, movement_id)

        if movement is None:
            return False

        session.delete(movement)
        session.commit()

        return True

def get_products_with_category_and_supplier():
    with SessionLocal() as session:
        stmt = (
            select(
                Product.name.label("product_name"),
                Category.name.label("category_name"),
                Supplier.name.label("supplier_name"),
            )
            .join(Category, Product.category_id == Category.id)
            .join(Supplier, Product.supplier_id == Supplier.id)
        )

        return session.execute(stmt).all()
    
def get_movements_with_product():
    with SessionLocal() as session:
        stmt = (
            select(
                Stock_movement.id.label("movement_id"),
                Stock_movement.quantity,
                Stock_movement.movement_type,
                Product.name.label("product_name"),
            )
            .join(Product, Stock_movement.product_id == Product.id)
        )

        return session.execute(stmt).all()
    
def get_products_count_by_category():
    with SessionLocal() as session:
        stmt = (
            select(
                Category.name.label("category_name"),
                func.count(Product.id).label("product_count"),
            )
            .join(Product, Product.category_id == Category.id)
            .group_by(Category.id)
        )

        return session.execute(stmt).all()
    
def get_products_count_by_supplier():
    with SessionLocal() as session:
        stmt = (
            select(
                Supplier.name.label("supplier_name"),
                func.count(Product.id).label("product_count"),
            )
            .join(Product, Product.supplier_id == Supplier.id)
            .group_by(Supplier.id)
        )

        return session.execute(stmt).all()

def get_current_stock_by_product():
    with SessionLocal() as session:
        stmt = (
            select(
                Product.name.label("product_name"),
                func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                ).label("current_stock"),
            )
            .join(Stock_movement, Stock_movement.product_id == Product.id)
            .group_by(Product.id)
        )

        return session.execute(stmt).all()
    
def get_low_stock_products():
    with SessionLocal() as session:
        stmt = (
            select(
                Product.name.label("product_name"),
                Product.min_quantity,
                func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                ).label("current_stock"),
            )
            .join(Stock_movement, Stock_movement.product_id == Product.id)
            .group_by(Product.id)
            .having(func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                ) < Product.min_quantity)
        )

        return session.execute(stmt).all()

def get_low_stock_products():
    with SessionLocal() as session:
        stmt = (
            select(
                Product.name.label("product_name"),
                Product.min_quantity,
                func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                ).label("current_stock"),
            )
            .join(Stock_movement, Stock_movement.product_id == Product.id)
            .group_by(Product.id)
            .having(func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                ) < Product.min_quantity)
        )

        return session.execute(stmt).all()

def get_total_purchase_value():
    with SessionLocal() as session:
        stmt = (
            select(
                func.sum(Product.purchase_price * func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                )).label("total_purchase_value")
            )
            .join(Stock_movement, Stock_movement.product_id == Product.id)
        )

        return session.execute(stmt).scalar()

def get_total_selling_value():
    with SessionLocal() as session:
        stmt = (
            select(
                func.sum(Product.selling_price * func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                )).label("total_selling_value")
            )
            .join(Stock_movement, Stock_movement.product_id == Product.id)
        )

        return session.execute(stmt).scalar()
    
def get_potential_profit():
    with SessionLocal() as session:
        stmt = (
            select(
                func.sum((Product.selling_price - Product.purchase_price) * func.sum(
                    case(
                        (Stock_movement.movement_type == "in", Stock_movement.quantity),
                        (Stock_movement.movement_type == "out", -Stock_movement.quantity),
                        else_=0,
                    )
                )).label("potential_profit")
            )
            .join(Stock_movement, Stock_movement.product_id == Product.id)
        )

        return session.execute(stmt).scalar()

