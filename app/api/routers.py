import os
from typing import Any, Optional

import httpx
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.core.logger import AffordmedLogger
from app.core.mock_data import MOCK_DEPOTS, MOCK_NOTIFICATIONS, MOCK_VEHICLES
from app.models.schemas import Depot, Notification, PaginatedNotifications, Vehicle

api_router = APIRouter(prefix="/api", tags=["Campus API"])

_EVALUATION_BASE = os.getenv(
    "EVALUATION_SERVICE_URL", "http://4.224.186.213/evaluation-service"
)


def _auth_headers() -> dict[str, str] | None:
    """
    Builds the Authorization header dict only when ACCESS_CODE is present in
    the environment. Returns None when the variable is absent so callers can
    decide whether to proceed or fall back immediately.
    """
    code = os.getenv("ACCESS_CODE")
    if not code:
        return None
    return {"Authorization": f"Bearer {code}"}


async def _fetch_remote(path: str, fallback: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Attempts an authenticated GET against the evaluation service.
    Falls back to the supplied local dataset on any failure — missing credential,
    network timeout, non-2xx response, or malformed JSON.
    """
    headers = _auth_headers()
    if headers is None:
        await AffordmedLogger("WARNING", f"ACCESS_CODE not set — skipping remote fetch for {path}")
        return fallback

    url = f"{_EVALUATION_BASE}{path}"
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
    except Exception as exc:
        await AffordmedLogger(
            "WARNING",
            f"Remote fetch failed for {url} ({type(exc).__name__}: {exc}) — serving local fallback",
        )
        return fallback


@api_router.get("/depots", response_model=list[Depot])
async def get_depots() -> JSONResponse:
    data = await _fetch_remote("/depots", MOCK_DEPOTS)
    await AffordmedLogger("INFO", f"GET /api/depots — returned {len(data)} records")
    return JSONResponse(content=data)


@api_router.get("/vehicles", response_model=list[Vehicle])
async def get_vehicles() -> JSONResponse:
    data = await _fetch_remote("/vehicles", MOCK_VEHICLES)
    await AffordmedLogger("INFO", f"GET /api/vehicles — returned {len(data)} records")
    return JSONResponse(content=data)


@api_router.get("/notifications", response_model=PaginatedNotifications)
async def get_notifications(
    limit: int = Query(default=10, ge=1, le=50, description="Number of results per page"),
    page: int = Query(default=1, ge=1, description="1-based page index"),
    notification_type: Optional[str] = Query(
        default=None, description="Filter by type: Alert | Info | Warning"
    ),
) -> JSONResponse:
    dataset = MOCK_NOTIFICATIONS

    if notification_type:
        dataset = [n for n in dataset if n["type"].lower() == notification_type.lower()]

    total = len(dataset)
    start = (page - 1) * limit
    page_slice = dataset[start : start + limit]

    await AffordmedLogger(
        "INFO",
        f"GET /api/notifications — page={page}, limit={limit}, type={notification_type}, returned={len(page_slice)}/{total}",
    )

    return JSONResponse(
        content={"total": total, "page": page, "limit": limit, "results": page_slice}
    )
