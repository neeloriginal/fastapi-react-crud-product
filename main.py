from fastapi import FastAPI
from models import Product
app = FastAPI()

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

@app.get("/products")
def get_all_productx():
    return products
 