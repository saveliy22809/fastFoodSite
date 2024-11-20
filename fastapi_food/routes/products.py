from fastapi import APIRouter, HTTPException
from fastapi_food.models import Product
from fastapi_food.database import SessionLocal

router = APIRouter()

@router.get("/products")
def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    return products

@router.post("/products")
def create_product(product: Product):
    db = SessionLocal()
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    db = SessionLocal()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.price = product.price
    db_product.stock = product.stock
    db.commit()
    db.refresh(db_product)
    return db_product
