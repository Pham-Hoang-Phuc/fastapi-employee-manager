from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from schemas import EmployeeCreate, TokenData
from model import Employee
from sqlalchemy.orm import Session
import bcrypt
from database import get_db


SECRET_KEY = "83daa0256a2289b0fb23693bf1f6034d44396675749244721a2b20e896e11662"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_hash_password(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8')


def verify_password(plain_password, hashed_password):
    password_byte = plain_password.encode('utf-8')
    hashed_byte = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte, hashed_byte)


def authenticate_user(db: Session, employee_name: str, password):
    employee = db.query(Employee).filter_by(username=employee_name).one_or_none()
    if not employee:
        return False
    if not verify_password(password, employee.hashed_password):
        return False
    return employee


def create_access_token(data: dict, expires_delta: timedelta | None = None):

    to_encoder = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encoder.update({"exp": expire})
    encoder_jwt = jwt.encode(to_encoder, SECRET_KEY, algorithm=ALGORITHM)
    return encoder_jwt


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="COULD NOT VALIDATE CREDENTIAL",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    employee = db.query(Employee).filter_by(username= token_data.username).one_or_none()
    if employee is None:
        raise credential_exception
    return employee


async def get_current_active_user(current_user: EmployeeCreate = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
