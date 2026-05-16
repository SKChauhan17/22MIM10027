from pydantic import BaseModel, Field


class Depot(BaseModel):
    id: int
    name: str
    location: str
    capacity: int


class Vehicle(BaseModel):
    id: int
    depot_id: int
    type: str
    # Constrained to the domain values understood by the maintenance scheduler.
    status: str = Field(..., pattern=r"^(Active|Maintenance|In Transit)$")
    last_maintenance_date: str


class Notification(BaseModel):
    id: int
    type: str = Field(..., pattern=r"^(Alert|Info|Warning)$")
    message: str
    is_read: bool
    timestamp: int


class PaginatedNotifications(BaseModel):
    total: int
    page: int
    limit: int
    results: list[Notification]
