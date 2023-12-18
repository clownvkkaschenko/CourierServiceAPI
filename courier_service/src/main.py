import pytz
from fastapi import FastAPI
from src.delivery.routers import delivery_router
from src.users.routers import user_router

from .configs import TIMEZONE

app = FastAPI(title='Courier Service API', description='Прототип API сервиса курьерской доставки.')


app.include_router(user_router)
app.include_router(delivery_router)

app.timezone = pytz.timezone(f'{TIMEZONE}')
