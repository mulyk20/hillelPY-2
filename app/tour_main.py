from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

import app.tour_config
from api_router.api_products import api_router_products
from api_router.api_users import api_router_users
from api_router.api_visitors import api_router_visitors
from app.tour_database import create_tables
# from web_router.web import web_router


def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    debug=app.tour_config.DEBUG,
    lifespan=lifespan,
)

app.include_router(api_router_products)
app.include_router(api_router_users)
app.include_router(api_router_visitors)
# app.include_router(web_router)
