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



    TODO: "Добавление пользователей"
    TODO: "Получение пользователя по id"
    TODO: "Изменение данных пользователей(имя)"
    TODO: "Изменение пароля пользователя"
    TODO: "Удаление пользователей"


class ChatManager:
    # Класс управления чатами

    def __init__(self, session_manager: SessionManager) -> None:

        self.SessionLocal = session_manager.SessionLocal
        self.engine = session_manager.engine

    def get_session(self) -> Session:
        # Метод создания и возвращения сессии

        session = self.SessionLocal()
        return session

    def create_chat(
        self,
        user_id: int,
        name: str,
        provider: str = "Mistral",
        status: bool = True,
        chat_system_prompt: str = "Ты — персональный помощник"
        ) -> models.Chat:
        # Метод создания чата

        with self.get_session() as session:
            chat = models.Chat(
                user_id = user_id,
                name=name,
                provider=provider,
                status=status,
                chat_system_prompt=chat_system_prompt
            )

            session.add(chat)
            session.commit()

            return chat

    def get_chat_by_id(
        self,
        chat_id: int
        ) -> models.Chat | None:
        # Поиск чата по id

        with self.get_session() as session:
            return session.query(models.Chat).get(chat_id)

    def get_all_chats(
        self
    ) -> list[models.Chat] | list:
        # Поиск всех чатов

        with self.get_session() as session:
            all_chats = session.query(models.Chat).all()

        return all_chats

    def update_chat_name(
            self,
            chat_id: int,
            new_name: str
            ) -> bool:
        # Изменение названия чата

        with self.get_session() as session:
            chat = self.get_chat_by_id(chat_id)

            if chat != None:
                chat.name = new_name
                session.commit()
                return True

            return False

    def update_status_chat(
            self,
            chat_id: int,
            new_status: bool,
            ) -> bool:
        # Обновление статуса чата

        with self.get_session() as session:
TODO: "======================Тут остановился===================="
    """По аналогии с update_chat_name"""
            chat = self тута дописывать
TODO: "======================Тут остановился===================="



    TODO: "Удаление чатов"


class MessageManager:
    # Класс управления сообщениями
    pass
    TODO: "Добавление сообщений"
    TODO: "Получение сообщений по id"
    TODO: "Получение всех сообщений"
    TODO: "Удаление сообщений"

TODO: "Класс инструкций"
    TODO: "Создание инструкций"
    TODO: "Получение инструкций по id"
    TODO: "Обновление данных в инструкциях"
    TODO: "Удаление инструкций"

TODO: "Класс задач"
    TODO: "Создание новой задачи"
    TODO: "Получение задачи по id"
    TODO: "Получение всех задач"
    TODO: "Удаление задачи"

TODO: "Класс сессий обучения"
    TODO: "Создание новой сессии обучения"
    TODO: "Получение сессии обучения по id"
    TODO: "Получение всех сессий обучения"
    TODO: "Удаление сессии обучения"

def _create_admin() -> None:
    # Функция создания админа
    pass

