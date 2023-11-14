from datetime import datetime
from typing import List, Optional
from pydantic import UUID4, BaseModel, Field
from app.domain_types.schemas.base_search_types import BaseSearchFilter, BaseSearchResults

class EventCreateModel(BaseModel):
    UserId                : UUID4                 = Field(description="Id of the User")
    TenantId              : UUID4                 = Field(description="Tenant Id of the User")
    Action                : str                   = Field(min_length=2, max_length=256, description="Action of the Event")
    EventType             : str                   = Field(min_length=2, max_length=128, description="Type of the Event")
    Timestamp             : datetime              = Field(default=None, description="Timestamp of the Event")
    Attributes            : Optional[dict | None] = Field(default=None, description="Attributes of the Event")
    AppVersion            : Optional[str | None]  = Field(default=None, min_length=2, max_length=16, description="App version of the Event")
    Platform              : Optional[str | None]  = Field(default=None, min_length=2, max_length=16, description="Platform of the Event")
    DeviceType            : Optional[str | None]  = Field(default=None, min_length=2, max_length=64, description="Device type of the Event")
    DeviceId              : Optional[str | None]  = Field(default=None, min_length=2, max_length=128, description="Device id of the Event")
    DaysSinceRegistration : Optional[int | None]  = Field(default=None, description="Days since registration of the Event")


class EventUpdateModel(BaseModel):
    pass

class EventSearchFilter(BaseSearchFilter):
    UserId   : Optional[UUID4]
    TenantId : Optional[UUID4]
    Action   : Optional[str]
    EventType: Optional[str]
    Attribute: Optional[str]
    FromDate : Optional[datetime]
    ToDate   : Optional[datetime]

class EventResponseModel(BaseModel):
    id                    : UUID4                   = Field(description="Id of the Event")
    UserId                : str                 = Field(description="Id of the User")
    TenantId              : UUID4                 = Field(description="Tenant Id of the User")
    Action                : str                   = Field(min_length=2, max_length=256, description="Action of the Event")
    EventType             : str                   = Field(min_length=2, max_length=128, description="Type of the Event")
    Timestamp             : datetime              = Field(default=None, description="Timestamp of the Event")
    Attributes            : Optional[dict | None] = Field(default=None, description="Attributes of the Event")
    AppVersion            : Optional[str | None]  = Field(default=None, min_length=2, max_length=16, description="App version of the Event")
    Platform              : Optional[str | None]  = Field(default=None, min_length=2, max_length=16, description="Platform of the Event")
    DeviceType            : Optional[str | None]  = Field(default=None, min_length=2, max_length=64, description="Device type of the Event")
    DeviceId              : Optional[str | None]  = Field(default=None, min_length=2, max_length=128, description="Device id of the Event")
    DaysSinceRegistration: Optional[int | None]   = Field(default=None, description="Days since registration of the Event")


class EventSearchResults(BaseSearchResults):
    Items: List[EventResponseModel] = []

