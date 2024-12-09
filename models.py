import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publishers' 

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))
    books = relationship('Book', back_populates='publisher')  


class Book(Base):
    __tablename__ = 'books'  
    
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publishers.id')) 
    publisher = relationship('Publisher', back_populates='books')  
    stocks = relationship('Stock', back_populates='book')  

class Shop(Base):
    __tablename__ = 'shops'  

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    stocks = relationship('Stock', back_populates='shop') 


class Stock(Base):
    __tablename__ = 'stocks' 

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'), nullable=False) 
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shops.id'), nullable=False)  
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship('Book', back_populates='stocks')
    shop = relationship('Shop', back_populates='stocks')
    sales = relationship('Sale', back_populates='stock') 


class Sale(Base):
    __tablename__ = 'sales'  

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)  
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'), nullable=False)  
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship('Stock', back_populates='sales') 
