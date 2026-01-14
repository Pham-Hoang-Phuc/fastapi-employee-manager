from fastapi import FastAPI, Query, Path, Body, Depends
from sqlalchemy.orm import Session

import crub
from database import engine, get_db
from model import Base
from schemas import EmployeeBase, EmployeeCreate, EmployeePublic, Departments

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register")
async def resiger_employee(
    *,
    employee: EmployeeCreate = Body(
        example={
            "username": "example_name",
            "email": "example@gmail.com",
            "password": "12345678@",
            "salary": 15000
        }
    ),
    department: Departments,
    db: Session = Depends(get_db)
):
    new_employee_data = employee.model_dump()

    new_employee_data["department"] = department.value

    return crub.create_employee(db, employee=new_employee_data)


@app.get("/employees")
async def show_all_employees(
    db: Session = Depends(get_db)
):
    return crub.get_all_employees(db)


@app.put("/employee/{user_id}/department")
async def change_department(
    *,
    user_id: int = Path(...),
    db: Session = Depends(get_db),
    new_department : Departments,
    user_password:str = Query(..., min_length=8)
):
    return crub.change_department(db, new_department.value, user_id, user_password)


@app.put("/employee/{user_id}/department/delete")
async def delete_employee(
    *,
    user_id: int = Path(...),
    user_password: str = Query(..., min_length=8),
    db: Session = Depends(get_db)
):
    return crub.delete_employee(db, user_id, user_password)