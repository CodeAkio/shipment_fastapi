from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from app.schemas import ShipmentCreate, ShipmentRead, ShipmentStatus, ShipmentUpdate

app = FastAPI()


shipments = {
    1234: {
        "id": 1234,
        "weight": 0.6,
        "content": "Grassware",
        "status": "Placed",
    },
    1235: {
        "id": 1235,
        "weight": 2.1,
        "content": "Steel rods",
        "status": "Delivered",
    },
    1236: {
        "id": 1236,
        "weight": 0.9,
        "content": "Books",
        "status": "In Transit",
    },
    1237: {
        "id": 1237,
        "weight": 3.5,
        "content": "Ceramic plates",
        "status": "Pending",
    },
    1238: {
        "id": 1238,
        "weight": 1.2,
        "content": "Electronics",
        "status": "Shipped",
    },
    1239: {
        "id": 1239,
        "weight": 4.0,
        "content": "Office chairs",
        "status": "Delivered",
    },
}


@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int | None = None) -> ShipmentRead:
    if not id:
        id = max(shipments.keys())
        return shipments[id]

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found",
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, Any]:
    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "status": "Placed",
    }

    return {"id": new_id}


@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return {field: shipments[id][field]}


@app.put("/shipment")
def update_shipment(
    id: int,
    content: str,
    weight: float,
    status: str,
) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status,
    }

    return shipments[id]


@app.patch("/shipment", response_model=ShipmentRead)
def patch_shipment(
    id: int,
    body: ShipmentUpdate,
) -> ShipmentRead:
    shipment = shipments[id]
    shipment.update(body)

    shipments[id] = shipment

    return shipments[id]


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found",
        )

    shipments.pop(id)
    return {"detail": f"Shipment {id} deleted successfully"}


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
