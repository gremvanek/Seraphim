from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.models import AbstractAdmin
from starlette.requests import Request

from models import Category, SubCategory, Product  # Импортируем модели


class Admin(AbstractAdmin):
    pass


async def on_after_register(user, request: Request):
    print(f"User {user.username} has been registered")


app = FastAPI()

admin_app.add_page(Admin(name="Dashboard", icon="fa fa-dashboard"))
admin_app.add_model(Category, name="Category", icon="fa fa-folder")
admin_app.add_model(SubCategory, name="SubCategory", icon="fa fa-folder-open")
admin_app.add_model(Product, name="Product", icon="fa fa-product-hunt")


@app.on_event("startup")
async def startup():
    await admin_app.init(
        admin_secret="secret",
        login_providers=[UsernamePasswordProvider(admin_app.auth)],
    )


app.mount("/admin", admin_app)
