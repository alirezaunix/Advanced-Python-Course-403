from sqlalchemy import create_engine, Column, Integer, String,or_ #
from sqlalchemy.orm import sessionmaker,declarative_base #

engine = create_engine('sqlite:///people.db') #

Base = declarative_base() #

class Person(Base): #
    __tablename__ = 'people' #
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

Base.metadata.create_all(engine) #


Session = sessionmaker(bind=engine) #
session = Session() #

p1 = session.query(Person).filter(Person.firstname=="Emily",Person.age>30).first()

print(p1.firstname,p1.lastname,p1.age)

session.delete(p1)
session.commit()