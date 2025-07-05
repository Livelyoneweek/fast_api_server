from pydantic import BaseModel, Field, ConfigDict

class CompanyCreate(BaseModel):
    name: str = Field(..., max_length=100)
    address: str

class CompanyRead(CompanyCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)   
