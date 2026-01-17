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
    hashed_password: str = Field(..., min_length=8, description="mật khẩu cần hơn 8 kí tự")
    disabled: bool | None = Field(False)
    salary: float = Field(None, gt=0)

class EmployeePublic(EmployeeBase):
    id: int 


# Token for authenticate
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None