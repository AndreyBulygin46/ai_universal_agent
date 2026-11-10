# Файл управление базой данных
import config
from database import models

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

class SessionManager:

    # Класс управления сессиями БД
    def __init__(self) -> None:
        self.engine = create_engine(config.BaseConfig.DATA_BASE.DB_URL)
        self.SessionLocal = sessionmaker(bind=self.engine, expire_on_commit=False)

    def get_session(self) -> Session:
        # Метод создания и возвращения сессии
        session = self.SessionLocal()
        return session

    def init_db(self) -> None:
        # Метод инициализации БД
        with self.SessionLocal() as session:
            models.Base.metadata.create_all(self.engine) # Создание таблиц
            session.commit()

print(models.Base.metadata.tables)

TODO: "Добавление пользователей"
TODO: "Получение пользователя по id"
TODO: "Изменение данных пользователей(имя)"
TODO: "Изменение пароля пользователя"
TODO: "Удаление пользователей"

TODO: "Добавление чатов"
TODO: "Получение чатов по id"
TODO: "Изменение чатов(название)"
TODO: "Удаление чатов"

TODO: "Добавление сообщений"
TODO: "Получение сообщений по id"
TODO: "Получение всех сообщений"
TODO: "Удаление сообщений"

TODO: "Создание инструкций"
TODO: "Получение инструкций по id"
TODO: "Обновление данных в инструкциях"
TODO: "Удаление инструкций"

TODO: "Создание новой задачи"
TODO: "Получение задачи по id"
TODO: "Получение всех задач"
TODO: "Удаление задачи"

TODO: "Создание новой сессии обучения"
TODO: "Получение сессии обучения по id"
TODO: "Получение всех сессий обучения"
TODO: "Удаление сессии обучения"


def _create_admin() -> None:
    # Функция создания админа
    pass

