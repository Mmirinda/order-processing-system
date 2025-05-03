pip install -r requirements.txt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class OrderRequest(BaseModel):
    product_id: int
    quantity: int
    customer_name: str
    delivery_address: str

@app.post("/order/")
async def create_order(order: OrderRequest):
    billing_response = requests.post("http://billing-service/api/bill", json=order.dict())
    if billing_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Billing service error")
      
    inventory_response = requests.post("http://inventory-service/api/inventory", json=order.dict())
    if inventory_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Inventory service error")

    delivery_response = requests.post("http://delivery-service/api/delivery", json=order.dict())
    if delivery_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Delivery service error")

    notification_response = requests.post("http://notification-service/api/notify", json={"message": f"Order for {order.customer_name} placed successfully"})
    if notification_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Notification service error")

    return {"message": "Order placed successfully"}
