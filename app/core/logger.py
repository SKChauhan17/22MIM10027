import os
import time
import httpx

_LOGGING_URL = os.getenv("LOGGING_URL", "https://test-server-endpoint.com/log")
_PACKAGE = "Afford Medical Technologies Private Limited"


async def AffordmedLogger(log_level: str, message: str) -> None:
    """
    Ships a structured log event to the centralized logging endpoint.
    Fire-and-forget: exceptions are suppressed so the logging path
    never interrupts the primary request lifecycle.
    """
    payload = {
        "timestamp": int(time.time()),
        "log_level": log_level,
        "message": message,
        "package": _PACKAGE,
    }

    # Include Authorization only when ACCESS_CODE is explicitly set in the environment.
    # Never fall back to a hardcoded value — credentials must not live in source.
    headers: dict[str, str] = {"Content-Type": "application/json"}
    access_code = os.getenv("ACCESS_CODE")
    if access_code:
        headers["Authorization"] = f"Bearer {access_code}"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            await client.post(_LOGGING_URL, json=payload, headers=headers)
    except Exception:
        pass