from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False)
    email = Column(String(20), unique=True, index=True)
    department = Column(String(10))
    hashed_password = Column(String(20))
    disabled = Column(Boolean)
    salary = Column(Float)