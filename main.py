from fastapi import FastAPI, Query, Path, Body, Depends
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import crud
from authen import get_current_active_user, get_hash_password
from database import engine, get_db
from model import Base
from schemas import EmployeeBase, EmployeeCreate, EmployeePublic, Departments, TokenData, Token


Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/token", response_model=Token)
async def login_for_access_token(
    db: Session = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return crud.authenticate(db, form_data)


@app.post("/register")
async def resiger_employee(
    *,
    employee: EmployeeCreate = Body(
        example={
            "username": "example_name",
            "email": "example@gmail.com",
            "hashed_password": "12345678@",
            "salary": 15000
        }
    ),
    department: Departments,
    db: Session = Depends(get_db)
):
    new_employee_data = employee.model_dump()

    new_employee_data["department"] = department.value
    new_employee_data["hashed_password"] = get_hash_password(new_employee_data["hashed_password"])
    return crud.create_employee(db, employee=new_employee_data)


@app.get("/employees")
async def show_all_employees(
    current_user: EmployeePublic = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return crud.get_all_employees(db)


@app.put("/employee/{user_id}/department")
async def change_department(
    *,
    user_id: int = Path(...),
    db: Session = Depends(get_db),
    new_department : Departments,
    user_password:str = Query(..., min_length=8)
):
    return crud.change_department(db, new_department.value, user_id, user_password)


@app.put("/employee/{user_id}/department/delete")
async def delete_employee(
    *,
    user_id: int = Path(...),
    user_password: str = Query(..., min_length=8),
    db: Session = Depends(get_db)
):
    return crud.delete_employee(db, user_id, user_password)