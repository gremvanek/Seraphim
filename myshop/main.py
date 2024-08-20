# from fastapi import FastAPI
# from .database import engine, Base, database
# from .routers import categories, products, subcategories, cart

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# app.include_router(categories.router, prefix="/api")
# app.include_router(products.router, prefix="/api")
# app.include_router(subcategories.router, prefix="/api")
# app.include_router(cart.router, prefix="/api")

# @app.get("/")
# async def root():
#     return {"message": "Seraphim"}

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("myshop/favicon.ico")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@app.post("/subcategories/", response_model=schemas.SubCategory)
def create_subcategory(
    subcategory: schemas.SubCategoryCreate, db: Session = Depends(get_db)
):
    return crud.create_subcategory(db=db, subcategory=subcategory)


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.post("/cart_items/", response_model=schemas.CartItem)
def create_cart_item(cart_item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    return crud.create_cart_item(db=db, cart_item=cart_item)


@app.get("/cart_items/{user_id}", response_model=list[schemas.CartItem])
def read_cart_items(user_id: int, db: Session = Depends(get_db)):
    return crud.get_cart_items(db, user_id=user_id)
