from enum import Enum
from random import randint
from pydantic import BaseModel, Field


def random_destination():
    return randint(11000, 11999)


class ShipmentStatus(str, Enum):
    Placed = "Placed"
    InTransit = "In Transit"
    OutForDelivery = "Out for Delivery"
    Delivered = "Delivered"


class Shipment(BaseModel):
    content: str = Field(max_length=30)
    weight: float = Field(
        le=25,
        gt=1,
        description="Weight in kg, must be between 1 and 25",
    )
    status: str | None = Field(
        default_factory=random_destination,
        description="Status of the shipment, defaults to a random destination code between 11000 and 11999",
    )
    status: ShipmentStatus = Field(
        default=ShipmentStatus.Placed,
        description="Status of the shipment, defaults to 'Placed'",
    )
