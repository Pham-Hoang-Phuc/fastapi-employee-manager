from sqlalchemy.orm import Session
from model import Employee
from fastapi import HTTPException

def create_employee(db: Session, employee: dict):
    new_employee = Employee(**employee)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_all_employees(db: Session):
    return db.query(Employee).all()

def change_department(db: Session, new_department: str, user_id: int, user_password: str):
    employee = db.query(Employee).filter_by(id = user_id, password = user_password).first()

    if not employee:
        raise HTTPException(status_code=404, detail="NOT FOUND")
    
    employee.department = new_department
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(db: Session, user_id: int, user_password: str):
    employee = db.query(Employee).filter_by(id= user_id, password= user_password).first()

    if not employee:
        raise HTTPException(status_code=404, detail="NOT FOUND")
    
    db.delete(employee)
    db.commit()
    return {
        "message": "DELETED",
        "employee": employee
    }