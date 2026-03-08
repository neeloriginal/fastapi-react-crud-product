from fastapi import Depends, FastAPI
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine) 

@app.get('/')
def greet():
    return 'hello world'

products = [
    Product(id=1, name="laptop", description="this is a laptop", price=50000, quantity=10),
    Product(id=2, name="phone", description="this is a phone", price=30000, quantity=20),
    Product(id=3, name="tablet", description="this is a tablet", price=20000, quantity=15),
    Product(id=4, name="desktop", description="this is a desktop", price=40000, quantity=5),
    Product(id=5, name="headphones", description="these are headphones", price=5000, quantity=30)
]

# def init_db():
#     db = session()
#     for product in products:
#         db_product = database_models.Product(
#             id=product.id,
#             name=product.name,
#                 description=product.description,
#                 price=product.price,
#                 quantity=product.quantity
#             )
#             db.add(db_product)
#         db.commit()
# init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/product")
def get_all_product(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        return product
    return {"error": "Product not found"}

@app.post("/product")
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

@app.put("/product/{id}")
def update_product(id: int, updated_product: Product, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        for key, value in updated_product.dict().items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
    return {"error": "Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted"}
    return {"error": "Product not found"} 