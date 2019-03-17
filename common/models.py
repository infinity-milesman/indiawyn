from sqlalchemy.orm import object_session

from config.constants import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy import Column, DateTime, Integer, String, Float, text, Boolean, Numeric, ForeignKey
from sqlalchemy.sql import func


class TimeStampedBaseModel(db.Model):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), server_default=func.now())
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())


class TimeStampedBaseModelWithUUID(TimeStampedBaseModel):
    __abstract__ = True
    uuid = Column(UUID, name='uuid')

