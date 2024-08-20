from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    slug: str
    price: float
    image_small: str
    image_medium: str
    image_large: str

class ProductCreate(ProductBase):
    subcategory_id: int

class Product(ProductBase):
    id: int
    subcategory_id: int

    class Config:
        orm_mode = True

class SubCategoryBase(BaseModel):
    name: str
    slug: str
    image: str

class SubCategoryCreate(SubCategoryBase):
    category_id: int

class SubCategory(SubCategoryBase):
    id: int
    category_id: int
    products: list[Product] = []

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str
    slug: str
    image: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    subcategories: list[SubCategory] = []

    class Config:
        orm_mode = True
