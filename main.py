from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import List
import random



class Price(BaseModel):
    name: str
    price: float


class Prices(BaseModel):
    prices: List[Price]


app = FastAPI()

commodities = {
    "Oil": 85.5,
    "Natural Gas": 3.2,
    "Gold": 1940.1,
    "Silver": 24.5
}


origins = [
    "https://localhost:3000",

]
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers = ["*"]
)


@app.get("/prices",response_model=Prices)
def get_prices():
    price_list =  [Price(name = name, price= round(price+random.uniform(-500,500),2)) for name,price in commodities.items()] 
    return Prices(prices= price_list)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)