from database import index as database
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Activities(database.GetConnection):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship('Person')