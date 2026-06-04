from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean, Text
from sqlalchemy.sql import func
from .connection import Base

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    job_code = Column(String(50), unique=True, nullable=False)
    position_name = Column(String(200), nullable=False)
    department = Column(String(100), nullable=False)
    vacancies = Column(Integer, default=1)
    applications_received = Column(Integer, default=0)
    status = Column(String(50), default='open')
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Candidate(Base):
    __tablename__ = "candidates"
    
    id = Column(Integer, primary_key=True, index=True)
    candidate_code = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    total_experience_years = Column(Float, default=0)
    highest_qualification = Column(String(100))
    ai_score = Column(Float)
    skills_match_percentage = Column(Float)
    research_score = Column(Float)
    application_status = Column(String(50), default='applied')
    created_at = Column(DateTime(timezone=True), server_default=func.now())