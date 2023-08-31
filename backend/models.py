from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dni = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable = False)

    entryMarks = relationship('EntryMarks', back_populates="user")
    exitMarks = relationship('ExitMarks', back_populates="user")


class EntryMarks(Base):
    __tablename__ = "entryMarks"

    id = Column(Integer, primary_key=True, index=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable = False)
    time = Column(Time, nullable = False)

    user = relationship('User', back_populates='entryMarks')


class ExitMarks(Base):
    __tablename__ = "exitMarks"

    id = Column(Integer, primary_key=True, index=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable = False)
    time = Column(Time, nullable = False)

    user = relationship('User', back_populates='exitMarks')


class Reports(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, index=False, autoincrement=True)
    start_date = Column(Date, nullable = False)
    end_date = Column(Date, nullable = False)
    status = Column(String, nullable = False)
    path = Column(String, nullable = True)