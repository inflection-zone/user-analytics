import json
import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, func, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy_json import mutable_json_type
from app.common.utils import generate_uuid4
from app.database.base import Base

class Event(Base):

    __tablename__ = "events"

    id                    = Column(String(36), primary_key=True, index=True, default=generate_uuid4)
    UserId                = Column(String(36), ForeignKey("users.id"), default=None, nullable=False)
    TenantId              = Column(String(36), default=None, nullable=False)
    Action                = Column(String(256), default=None, nullable=False)
    EventType             = Column(String(256), default=None, nullable=False)
    Attributes            = Column(mutable_json_type(dbtype=JSONB, nested=True), default=None, nullable=True)
    Timestamp             = Column(DateTime(timezone=True), server_default=func.now())
    AppVersion            = Column(String(16), default=None, nullable=True)
    Platform              = Column(String(16), default=None, nullable=True)
    DeviceType            = Column(String(64), default=None, nullable=True)
    DeviceId              = Column(String(128), default=None, nullable=True)
    DaysSinceRegistration = Column(Integer, default=None, nullable=True)

    def __repr__(self):
        jsonStr = json.dumps(self.__dict__)
        return jsonStr
