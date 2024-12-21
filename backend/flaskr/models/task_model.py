from enum import Enum
from sqlalchemy import String, Enum as SaEnum
from sqlalchemy.orm import Mapped, mapped_column
from flaskr.db import db
from datetime import datetime, timezone


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )
