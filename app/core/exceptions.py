from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logger import AffordmedLogger


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """
    Normalises FastAPI's verbose validation error output into a consistent
    client-facing shape. The raw Pydantic error tree is flattened so callers
    receive exactly one entry per offending field rather than a nested structure.
    """
    details = []
    for error in exc.errors():
        # 'loc' is a tuple of path segments; join them so the field is readable
        # (e.g. ("query", "limit") → "query.limit").
        field = ".".join(str(segment) for segment in error.get("loc", []))
        details.append({"field": field, "message": error.get("msg", "Invalid value")})

    await AffordmedLogger(
        "WARNING",
        f"Validation error on {request.method} {request.url.path}: {details}",
    )

    return JSONResponse(
        status_code=400,
        content={"error": "Validation Failed", "details": details},
    )


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Last-resort handler for any exception that escapes normal route handling.
    Stack traces are intentionally omitted from the response to avoid leaking
    internal implementation details to clients.
    """
    await AffordmedLogger(
        "ERROR",
        f"Unhandled {type(exc).__name__} on {request.method} {request.url.path}: {exc}",
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred.",
        },
    )
