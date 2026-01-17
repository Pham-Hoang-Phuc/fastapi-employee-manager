from sqlalchemy.orm import Session
from model import Employee
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from authen import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
import authen


def authenticate(db: Session, form_data: OAuth2PasswordRequestForm):
    user = authen.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authen.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


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
    employee = db.query(Employee).filter_by(id=user_id, password= user_password).first()
    if not employee:
        raise HTTPException(status_code=404, detail="NOT FOUND")
    db.delete(employee)
    db.commit()
    return {
        "message": "DELETED",
        "employee": employee
    }
