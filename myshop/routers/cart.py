from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from myshop.models import CartItem
from myshop.database import get_db, get_current_user

router = APIRouter()  # Создаем объект маршрутизатора


class CartItemRequest(BaseModel):
    product_id: int
    quantity: int


@router.post("/cart/")
def add_item_to_cart(
    item: CartItemRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
):
    cart_item = (
        db.query(CartItem)
        .filter_by(user_id=user_id, product_id=item.product_id)
        .first()
    )
    if cart_item:
        cart_item.quantity += item.quantity
    else:
        new_cart_item = CartItem(
            user_id=user_id, product_id=item.product_id, quantity=item.quantity
        )
        db.add(new_cart_item)
    db.commit()


@router.get("/cart/")
def get_cart(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    cart_items = db.query(CartItem).filter_by(user_id=user_id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return {"items": cart_items, "total": total}


@router.delete("/cart/{item_id}")
def delete_item_from_cart(
    item_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
):
    cart_item = db.query(CartItem).filter_by(user_id=user_id, id=item_id).first()
    if cart_item:
        db.delete(cart_item)
        db.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


@router.delete("/cart/")
def clear_cart(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    db.query(CartItem).filter_by(user_id=user_id).delete()
    db.commit()
