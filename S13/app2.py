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

#for line in open("/Users/alireza/Desktop/Advanced Python Course 403/S13/src.csv"):
#    p1=Person(firstname=line.split(",")[0],lastname=line.split(",")[1],age=int(line.split(",")[2]))
#    session.add(p1)
#    session.commit()

#1 data=session.query(Person).all()
#2 older_people = session.query(Person).filter(Person.age > 24).all()
#3 johns = session.query(Person).filter(Person.firstname == "John", Person.age > 20).all()
#4 johns_or_young = session.query(Person).filter(or_(Person.firstname == "John", Person.age < 23)).all()
#5 smiths = session.query(Person).filter(Person.firstname.like('%M%')).all()
#6 people_ordered_by_age = session.query(Person).order_by(Person.lastname.desc()).all()
#7 first_two_people = session.query(Person).limit(2).all()
