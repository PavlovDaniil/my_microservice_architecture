from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from fastapi import FastAPI


DATABASE_URL = "postgresql+psycopg2://user:1234@localhost:5432/db"

# 2. Создание движка и сессии
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# 3. Базовый класс и модель таблицы users
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
    # Добавь другие поля, если они есть
    def __repr__(self):
        return f"<User(id={self.id}, login='{self.user_name}', hashPassword='{self.password}')>"

# 4. Получение и вывод всех пользователей
users = session.query(User).all()

for user in users:
    print(user)
