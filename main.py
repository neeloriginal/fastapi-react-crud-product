from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],    
    allow_headers=["*"],
)
database_models.Base.metadata.create_all(bind=engine) 

@app.get('/')
def greet():
    return 'hello world'


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        return product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):

    db_product = database_models.Product(
        id=product.id,
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

@app.put("/products/{id}")
def update_product(id: int, updated_product: Product, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        for key, value in updated_product.dict().items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
    return {"error": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted"}
    return {"error": "Product not found"} 