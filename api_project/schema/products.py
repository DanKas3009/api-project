from pydantic import BaseModel

class Product(BaseModel):
    productcode: str
    productname: str
    productdescription: str = None
    buyprice: float
    
    class Config:
        from_attributes = True
