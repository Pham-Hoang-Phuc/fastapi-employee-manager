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