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

@app.get("/product")
def get_all_product():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/product")
def create_product(product: Product):
    products.append(product)
    return product

@app.put("/product/{id}")
def update_product(id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == id:
            products[index] = updated_product
            return updated_product
    return {"error": "Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            products.pop(index)
            return {"message": "Product deleted"}
    return {"error": "Product not found"} 