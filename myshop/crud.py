from sqlalchemy.orm import Session
from . import models, schemas

# CRUD для категорий
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# CRUD для подкатегорий
def get_subcategory(db: Session, subcategory_id: int):
    return db.query(models.SubCategory).filter(models.SubCategory.id == subcategory_id).first()

def get_subcategories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SubCategory).offset(skip).limit(limit).all()

def create_subcategory(db: Session, subcategory: schemas.SubCategoryCreate):
    db_subcategory = models.SubCategory(**subcategory.dict())
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory

def delete_subcategory(db: Session, subcategory_id: int):
    db_subcategory = db.query(models.SubCategory).filter(models.SubCategory.id == subcategory_id).first()
    if db_subcategory:
        db.delete(db_subcategory)
        db.commit()
    return db_subcategory

# CRUD для продуктов
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# CRUD для корзины
def get_cart_items(db: Session, user_id: int):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()

def create_cart_item(db: Session, cart_item: schemas.CartItemCreate):
    db_cart_item = models.CartItem(**cart_item.dict())
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def update_cart_item(db: Session, cart_item_id: int, quantity: int):
    db_cart_item = db.query(models.CartItem).filter(models.CartItem.id == cart_item_id).first()
    if db_cart_item:
        db_cart_item.quantity = quantity
        db.commit()
        db.refresh(db_cart_item)
    return db_cart_item

def delete_cart_item(db: Session, cart_item_id: int):
    db_cart_item = db.query(models.CartItem).filter(models.CartItem.id == cart_item_id).first()
    if db_cart_item:
        db.delete(db_cart_item)
        db.commit()
    return db_cart_item

def clear_cart(db: Session, user_id: int):
    db.query(models.CartItem).filter(models.CartItem.user_id == user_id).delete()
    db.commit()
