from pydantic import BaseModel, EmailStr, Field
from enum import Enum

class Departments(Enum):
    IT = "IT" 
    HR = "HR" 
    ENGINEERING = "Engineering" 
    SALES = "Sales" 
    MARKETING = "Marketing" 
    FINANCE = "Finance" 
    DATA = "Data"

class EmployeeBase(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    department: Departments | None = None

class EmployeeCreate(EmployeeBase):
    password: str = Field(..., min_length=8, description="mật khẩu cần hơn 8 kí tự")
    salary: float = Field(None, gt=0)

class EmployeePublic(EmployeeBase):
    id: int 