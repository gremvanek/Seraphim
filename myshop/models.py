from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    image = Column(String)

    subcategories = relationship("SubCategory", back_populates="category")

class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    image = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="subcategories")
    products = relationship("Product", back_populates="subcategory")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    image_small = Column(String)
    image_medium = Column(String)
    image_large = Column(String)
    price = Column(Float)
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"))

    subcategory = relationship("SubCategory", back_populates="products")

class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    user_id = Column(Integer)  # Связь с пользователем, замените на ForeignKey если есть таблица пользователей

    product = relationship("Product")
