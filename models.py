import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publishers'  # Изменено на множественное число

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))
    books = relationship('Book', back_populates='publisher')  # Исправлено на books


class Book(Base):
    __tablename__ = 'books'  # Оставлено как есть

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publishers.id'))  # Исправлено на 'publishers.id'
    publisher = relationship('Publisher', back_populates='books')  # Исправлено на books
    stocks = relationship('Stock', back_populates='book')  # Добавлено обратное отношение к Stock


class Shop(Base):
    __tablename__ = 'shops'  # Изменено на множественное число

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40))

    stocks = relationship('Stock', back_populates='shop')  # Исправлено на stocks


class Stock(Base):
    __tablename__ = 'stocks'  # Изменено на множественное число

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'), nullable=False)  # Исправлено на 'books.id'
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shops.id'), nullable=False)  # Исправлено на 'shops.id'
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship('Book', back_populates='stocks')
    shop = relationship('Shop', back_populates='stocks')
    sales = relationship('Sale', back_populates='stock')  # Исправлено на sales


class Sale(Base):
    __tablename__ = 'sales'  # Изменено на множественное число

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)  # Изменено на sq.Numeric
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'), nullable=False)  # Исправлено на 'stocks.id'
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship('Stock', back_populates='sales')  # Исправлено на sales