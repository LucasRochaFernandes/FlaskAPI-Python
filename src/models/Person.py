from database import index as database
from sqlalchemy import Column, Integer, String


class Person(database.GetConnection):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    age = Column(Integer)

    def __repr__(self):
        return '<Person {}>'.format(self.name)