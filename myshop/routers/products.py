from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from myshop.models import Product
from .. import crud, schemas, database

router = APIRouter()


@router.post("/products/", response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate, db: Session = Depends(database.get_db)
):
    return crud.create_product(db=db, product=product)


@router.get("/products/")
def get_products(
    skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)
):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@router.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(database.get_db)):
    db_product = crud.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
