from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker,declarative_base

engine = create_engine('sqlite:///books.db')
Base = declarative_base()

class Writer(Base):
    __tablename__ = 'writers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='writer')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    writer_id = Column(Integer, ForeignKey('writers.id'))
    writer = relationship('Writer', back_populates='books')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


new_writer = Writer(name="George Orwell")
book1 = Book(title="1984", writer=new_writer)
book2 = Book(title="Animal Farm", writer=new_writer)
session.add(new_writer)
session.add_all([book1, book2])
session.commit()
