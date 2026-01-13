from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "sqlite:///databse.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = Session()

    try:
        yield db
    finally:
        db.close()