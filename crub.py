from sqlalchemy.orm import Session
from model import Employee

def create_employee(db: Session, employee: dict):
    new_employee = Employee(**employee)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_all_employees(db: Session):
    return db.query(Employee).all()
