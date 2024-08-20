from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/cart/", response_model=schemas.CartItem)
def add_to_cart(cart_item: schemas.CartItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_cart_item(db=db, cart_item=cart_item)

@router.get("/cart/", response_model=list[schemas.CartItem])
def read_cart(user_id: int, db: Session = Depends(database.get_db)):
    cart_items = crud.get_cart_items(db, user_id=user_id)
    return cart_items

@router.put("/cart/{cart_item_id}", response_model=schemas.CartItem)
def update_cart(cart_item_id: int, quantity: int, db: Session = Depends(database.get_db)):
    return crud.update_cart_item(db=db, cart_item_id=cart_item_id, quantity=quantity)

@router.delete("/cart/{cart_item_id}", response_model=schemas.CartItem)
def remove_from_cart(cart_item_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_cart_item(db=db, cart_item_id=cart_item_id)

@router.delete("/cart/", response_model=list[schemas.CartItem])
def clear_cart(user_id: int, db: Session = Depends(database.get_db)):
    crud.clear_cart(db=db, user_id=user_id)
    return []
