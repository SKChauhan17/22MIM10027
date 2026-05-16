from typing import Optional

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.core.logger import AffordmedLogger
from app.core.mock_data import MOCK_DEPOTS, MOCK_NOTIFICATIONS, MOCK_VEHICLES
from app.models.schemas import Depot, Notification, PaginatedNotifications, Vehicle

api_router = APIRouter(prefix="/api", tags=["Campus API"])


@api_router.get("/depots", response_model=list[Depot])
async def get_depots() -> JSONResponse:
    await AffordmedLogger("INFO", "GET /api/depots — returning all depot records")
    return JSONResponse(content=MOCK_DEPOTS)


@api_router.get("/vehicles", response_model=list[Vehicle])
async def get_vehicles() -> JSONResponse:
    await AffordmedLogger("INFO", "GET /api/vehicles — returning all vehicle records")
    return JSONResponse(content=MOCK_VEHICLES)


@api_router.get("/notifications", response_model=PaginatedNotifications)
async def get_notifications(
    limit: int = Query(default=10, ge=1, le=50, description="Number of results per page"),
    page: int = Query(default=1, ge=1, description="1-based page index"),
    notification_type: Optional[str] = Query(default=None, description="Filter by type: Alert | Info | Warning"),
) -> JSONResponse:
    dataset = MOCK_NOTIFICATIONS

    if notification_type:
        dataset = [n for n in dataset if n["type"].lower() == notification_type.lower()]

    total = len(dataset)
    start = (page - 1) * limit
    end = start + limit
    page_slice = dataset[start:end]

    await AffordmedLogger(
        "INFO",
        f"GET /api/notifications — page={page}, limit={limit}, type={notification_type}, returned={len(page_slice)}/{total}",
    )

    return JSONResponse(
        content={
            "total": total,
            "page": page,
            "limit": limit,
            "results": page_slice,
        }
    )
