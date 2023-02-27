from pydantic import BaseModel

class Product(BaseModel):
    name: str
    category: str
    quantity: float
    packprice: float
    unitprice: float