# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# MySQL connection details
MYSQL_USERNAME = "root"    # Replace with your MySQL username
MYSQL_PASSWORD = "password"    # Replace with your MySQL password
MYSQL_HOST = "localhost"            # Replace with your MySQL host (usually 'localhost')
MYSQL_PORT = 3306                 # Default MySQL port is 3306
MYSQL_DATABASE = "todos_db"         # Replace with your MySQL database name

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


# SQLAlchemy engine, session, and base class configuration
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to provide the database session to the route handlers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
