from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# Information required to create a property
class HomeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=5, max_length=250)
    city: str = Field(min_length=2, max_length=100)
    state: str = Field(min_length=2, max_length=100)
    pincode: str = Field(min_length=4, max_length=10)


# Information returned by the API
class HomeResponse(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    pincode: str
    created_by: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)