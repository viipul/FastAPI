from pydantic import BaseModel,Field
from typing import Optional


class Employee(BaseModel):
    id: int = Field(...,gt=0)
    name : str=Field(...,min_length=3,max_length=50)
    department:str=Field(...,min_length=3,max_length=50)
    age:Optional[int]=Field(...,gt=0,lt=100)

