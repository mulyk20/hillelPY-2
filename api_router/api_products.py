from fastapi import APIRouter, HTTPException, status
from typing import List, Optional

from app.tour_schemas import NewProduct, CreatedProduct, UpdateProduct
import app.tour_dao as dao

api_router_products = APIRouter(
    prefix="/products",
    tags=["products"]
)

@api_router_products.post("/", response_model=CreatedProduct, status_code=status.HTTP_201_CREATED)
def create_product(product: NewProduct) -> CreatedProduct:
    created_product = dao.create_product(product.name, product.description, product.price, product.quantity, product.cover_url)
    if not created_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product creation failed")
    return created_product

@api_router_products.get("/", response_model=List[CreatedProduct])
def get_all_products():
    products = dao.get_all_products()
    return products

@api_router_products.get("/search", response_model=List[CreatedProduct])
def search_products(name: Optional[str] = None, limit: int = 100, skip: int = 0):
    products = dao.search_products(name=name, limit=limit, skip=skip)
    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found")
    return products

@api_router_products.put("/{product_id}", response_model=CreatedProduct)
def update_product(product_id: int, product: UpdateProduct) -> CreatedProduct:
    updated_product = dao.update_product(product_id, product.name, product.description, product.price, product.quantity, product.cover_url)
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated_product

@api_router_products.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    result = dao.delete_product(product_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return
