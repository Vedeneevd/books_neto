from os import times

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DSN
from models import Book, Shop, Stock, Publisher, Sale, Base
from datetime import date

DSN = DSN
engine = sqlalchemy.create_engine(DSN)


# сессия
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание объектов
publisher1 = Publisher(name='Азбука')
publisher2 = Publisher(name='Сигма')

book1 = Book(title='Капитанская дочка', publisher=publisher1)
book2 = Book(title='Руслан и Людмила', publisher=publisher1)
book3 = Book(title='Капитанская дочка', publisher=publisher2)
book4 = Book(title='Капитанская дочка', publisher=publisher2)

shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Дом книги')

stock1 = Stock(book=book1, shop=shop1, count=10)
stock2 = Stock(book=book2, shop=shop1, count=5)
stock3 = Stock(book=book3, shop=shop2, count=3)

sale1 = Sale(price=199.99, date_sale=date(2022, 10, 2), stock=stock1, count=2)
sale2 = Sale(price=299.99, date_sale=date(2021, 8, 24), stock=stock1, count=1)
sale3 = Sale(price=399.99, date_sale=date(2023, 5, 1), stock=stock3, count=1)

# Добавление объектов в сессию
session.add(publisher1)
session.add(publisher2)
session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(shop1)
session.add(shop2)
session.add(stock1)
session.add(stock2)
session.add(stock3)
session.add(sale1)
session.add(sale2)
session.add(sale3)

# Сохранение изменений в базе данных
session.commit()

publisher_input = input("Введите имя или идентификатор издателя: ")

# Попытка найти издателя по имени или идентификатору
if publisher_input.isdigit():
    publisher_id = int(publisher_input)
    publisher = session.query(Publisher).filter(Publisher.id == publisher_id).first()
else:
    publisher = session.query(Publisher).filter(Publisher.name == publisher_input).first()

if publisher:
    # Запрос фактов покупки книг этого издателя
    results = session.query(Sale).join(Stock).join(Book).filter(Book.publisher_id == publisher.id).all()


    for sale in results:
        book_title = sale.stock.book.title if sale.stock.book else "Неизвестно"
        shop_name = sale.stock.shop.name if sale.stock.shop else "Неизвестно"
        price = sale.price
        date = sale.date_sale

        print(f"{book_title:} | {shop_name:} | {price:} | {date}")
else:
    print("Издатель не найден.")

# Закрытие сессии
session.close()


