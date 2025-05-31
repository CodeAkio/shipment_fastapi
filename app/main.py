from fastapi import FastAPI

app = FastAPI()


@app.get("/shipment")
def get_shipment():
    return {
        "id": 1,
        "content": "Wooden table",
        "status": "In Transit",
    }
