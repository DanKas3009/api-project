from fastapi import FastAPI
from api_project.routes import product_routes

app = FastAPI()

# Include routes from country_routes
app.include_router(product_routes.router)

# Entry endpoint 
@app.get("/")
def root():
    return {"message": "Welcome to the REST Countries API using FastAPI"}
