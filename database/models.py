# База данных
from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass

class User(Base):
    # Модель пользователя
    __tablename__ = "users_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(25), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    display_name: Mapped[str] = mapped_column(String(25), default=f"User_default" )
    is_superuser: Mapped[bool] = mapped_column(default=False)

    # Связи
    chats: Mapped[list["Chat"]] = relationship(
        "Chat", back_populates="users", cascade="all, delete-orphan"
        )

class Chat(Base):

    # Модель чата
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    provider: Mapped[str] = mapped_column(String(100), default="Mistral")
    status: Mapped[bool] = mapped_column(default=True)
    chat_system_prompt: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Связи с другими моделями
    messages: Mapped[list["Message"]] = relationship(
        "Message", back_populates="chat", cascade="all, delete-orphan"
    )
    instructions: Mapped[list["Instruction"]] = relationship(
        "Instruction", back_populates="chat", cascade="all, delete-orphan"
    )
    tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="chat", cascade="all, delete-orphan"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users_table.id"), nullable=False, index=True
    )
    users: Mapped["User"] = relationship("User", back_populates="chats")

class Message(Base):

    # Модель сообщения
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(String(15), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    # Связь с моделью Chat
    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"), nullable=False, index=True
    )
    chat: Mapped["Chat"] = relationship("Chat", back_populates="messages")


class Instruction(Base):

    # Модель инструкций для модели ИИ
    __tablename__ = "instructions"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )

    # Связь с моделью Chat
    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"), nullable=False, index=True
    )
    chat: Mapped["Chat"] = relationship("Chat", back_populates="instructions")


class Task(Base):

    # Модель задач для модели ИИ
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(12), nullable=False, default="В процессе"
    )

    # Связи
    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"), nullable=False, index=True
    )
    chat: Mapped["Chat"] = relationship("Chat", back_populates="tasks")
    sessions: Mapped[list["TrainingSession"]] = relationship(
        "TrainingSession", back_populates="task"
    )


class TrainingSession(Base):

    # Модель сессии обучения модели ИИ
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    process: Mapped[str] = mapped_column(String(20), default="idle")

    # Связи
    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True
    )
    task: Mapped["Task"] = relationship(
        "Task", back_populates="sessions", passive_deletes="all"
    )