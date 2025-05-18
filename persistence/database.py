
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

CONNECTION = "mysql+pymysql://root:Scorpion/2601@localhost:3308/atm"

SessionLocal = sessionmaker(bind=create_engine(CONNECTION, echo=False))

Base = declarative_base()

