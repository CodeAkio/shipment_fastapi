from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:
    return {
        "id": id,
        "weight": 1.8,
        "content": "Wooden table",
        "status": "In Transit",
    }

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )