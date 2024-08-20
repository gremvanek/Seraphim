from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_category(db=db, category=category)

@router.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(database.get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/categories/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(database.get_db)):
    db_category = crud.delete_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
