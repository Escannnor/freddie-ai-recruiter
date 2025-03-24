from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./freddie.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

class Candidate(Base):
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    screening_answer = Column(Text, nullable=True)
    resume_link = Column(String, nullable=True)
    score = Column(Float, nullable=True)

def init_db():
    """
    Initializes the database by creating all tables.
    """
    Base.metadata.create_all(bind=engine)
