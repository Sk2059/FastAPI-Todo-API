from sqlalchemy import  String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime 

from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id:Mapped[int]=mapped_column(
        primary_key=True,
        index=True
    )

    title:Mapped[str]=mapped_column(
        String(255),
        nullable=False,
    )

    description:Mapped[str]=mapped_column(
        String(255),
        nullable=True,
    )

    completed:Mapped[bool]=mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    priority:Mapped[str]=mapped_column(
        String(50),
        nullable=False,
        default="medium"
    )

    created_at:Mapped[datetime]=mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    owner_id:Mapped[int]=mapped_column(
        ForeignKey("Users.id"),
        nullable=False
    )

    owner = relationship(
        "User",
        back_populates="tasks"
    )
