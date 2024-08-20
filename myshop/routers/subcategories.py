from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/subcategories/", response_model=schemas.SubCategory)
def create_subcategory(subcategory: schemas.SubCategoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_subcategory(db=db, subcategory=subcategory)

@router.get("/subcategories/", response_model=list[schemas.SubCategory])
def read_subcategories(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    subcategories = crud.get_subcategories(db, skip=skip, limit=limit)
    return subcategories

@router.get("/subcategories/{subcategory_id}", response_model=schemas.SubCategory)
def read_subcategory(subcategory_id: int, db: Session = Depends(database.get_db)):
    db_subcategory = crud.get_subcategory(db, subcategory_id=subcategory_id)
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return db_subcategory

@router.delete("/subcategories/{subcategory_id}", response_model=schemas.SubCategory)
def delete_subcategory(subcategory_id: int, db: Session = Depends(database.get_db)):
    db_subcategory = crud.delete_subcategory(db, subcategory_id=subcategory_id)
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail="Subcategory not found")
    return db_subcategory
