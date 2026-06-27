from datetime import date
from typing import Optional
from sqlalchemy import (
    Boolean,
    CheckConstraint, 
    Date,
    ForeignKey,
    Integer,
    Text,
    Float
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Supplier(Base):
    __tablename__ = "suppliers"

    __table_args__ = (
        CheckConstraint("length(name) > 0", name="check_name_length"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    phone: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(Text, nullable=True, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[Optional[date]] = mapped_column(Date, nullable=True) 
    
    products: Mapped[list["Product"]] = relationship(back_populates="supplier")


class Product(Base):
    __tablename__ = "product"

    __table_args__ = (
        CheckConstraint("purchase_price >= 0", name="check_purchase_price_non_negative"),
        CheckConstraint("selling_price >= 0", name="check_selling_price_non_negative"),
        CheckConstraint("min_quantity >= 0", name="check_min_quantity_non_negative")
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    sku: Mapped[int] = mapped_column(Integer, unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    supplier_id: Mapped[int] = mapped_column(ForeignKey('suppliers.id'), nullable=False)
    purchase_price: Mapped[float] = mapped_column(Float)
    selling_price: Mapped[float] = mapped_column(Float)
    min_quantity: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[date] = mapped_column(Date)
    
    # Связи
    supplier: Mapped["Supplier"] = relationship(back_populates="products")
    category: Mapped["Category"] = relationship(back_populates="products")
    movements: Mapped[list["Stock_movement"]] = relationship(back_populates="product") 


class Stock_movement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False) 
    movement_type: Mapped[str] = mapped_column(Text, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[date] = mapped_column(Date)
    
    # Связи
    product: Mapped["Product"] = relationship(back_populates="movements") # Добавлено