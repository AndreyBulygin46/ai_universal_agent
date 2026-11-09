# База данных
from config import BaseConfig

# Импорт моделей SQLAlchemy
from sqlalchemy import (create_engine,
                        String,
                        Text,
                        DateTime)
from sqlalchemy.orm import (sessionmaker,
                            DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship)

# Создаем объект базы данных
engine = create_engine(BaseConfig.DATA_BASE.DB_URL)


class Base(DeclarativeBase):
    pass


class Chat(Base):
    # Модель чата
    __tablename__ = "chats"  # Имя таблицы
    id: Mapped[int] = mapped_column(primary_key=True) # Идентификатор чата
    name: Mapped[str | None] = mapped_column(String(80), nullable=False, unique=True) # Имя чата
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), nullable=False) # Дата создания чата
    provider: Mapped[str] = mapped_column(String(100), default="Mistral") # Провайдер для чата, по умолчанию Mistral
    status: Mapped[bool] = mapped_column(default=True) # Статус чата (активный/неактивный)
    chat_sistem_promt: Mapped[str] = mapped_column(Text, nullable=True) # Системный промт для каждого чата отдельно

    TODO: 'ДОДЕЛАТЬ СВЯЗИ'
    messages: relationship(argument="Message", back_populates="chat", cascade="all, delete-orphan") # Связь с Message, связь с chat, удаление по родительскому каскадом
    instructions: relationship(argument="Instruction", back_populates="chat", cascade="all, delete-orphan") # Связь с Instruction, связь с chat, удаление по родительскому каскадом
    tasks: relationship(argument="Task", back_populates="chat", cascade="all, delete-orphan") # Связь с Task, связь с chat, удаление по родительскому каскадом
    # session Session

class Message(Base):
    # Модель сообщения
    __tablename__ = "messages"  # Имя таблицы
    id: Mapped[int] = mapped_column(primary_key=True) # Идентификатор сообщения
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id", nullable=False)) # Идентификатор чата

    TODO: 'Доделать дальше поля'

    TODO: 'ДОДЕЛАТЬ СВЯЗИ'
    chat: relationship("Chat", back_populates="messages")

class Instruction(Base):
    # Модель инструкций для модели ИИ
    # __tablename__ = "instruction" # Имя таблицы
    pass
    # Связи
    #  chat: relationship("Chat", back_populates="instructions")


class Task(Base):
    # Модель задач для модели ИИ
    pass
    # Связи
    # chat: relationship("Chat", back_populates="tasks")


class Session(Base):
    # Модель сессии обучения модели ии
    pass
    # Связи
    # chat: relationship("Chat", back_populates="sessions")

