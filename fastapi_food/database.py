from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных SQLite
DATABASE_URL = "sqlite:///./test.db"

# Создание соединения
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание базы данных
Base = declarative_base()

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функция для получения базы данных в маршрутах
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
