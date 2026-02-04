from sqlalchemy import Column, Date, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Revenue(Base):
    __tablename__ = "revenues"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    date = Column(Date, nullable=False)
    amount = Column(BYTEA, nullable=False)
    category = Column(BYTEA, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    date = Column(Date, nullable=False)
    amount = Column(BYTEA, nullable=False)
    category = Column(BYTEA, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
