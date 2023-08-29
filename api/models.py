from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship

from database import Base


class Reports(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, index=False, autoincrement=True)
    start_date = Column(Date, nullable = False)
    end_date = Column(Date, nullable = False)
    status = Column(String, nullable = False)
    path = Column(String, nullable = True)