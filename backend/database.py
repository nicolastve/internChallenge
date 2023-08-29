from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user = 'admin_user'
db_password = 'admin1234'
db_host = 'mysql'
db_port = '3306'
db_name = 'my_company'

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()