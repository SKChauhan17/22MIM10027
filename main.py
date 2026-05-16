from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routers import api_router
from app.core.exceptions import global_exception_handler, validation_exception_handler
from app.core.logger import AffordmedLogger

app = FastAPI(
    title="Campus Notifications & Vehicle Maintenance Scheduler API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ---------------------------------------------------------------------------
# CORS — permissive during development; tighten allow_origins for production.
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Exception handlers
# ---------------------------------------------------------------------------
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)


# ---------------------------------------------------------------------------
# Request logging middleware
# ---------------------------------------------------------------------------
@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    """
    Intercepts every inbound request to emit a structured INFO log,
    and catches unhandled exceptions to emit an ERROR log before re-raising.
    This ensures full observability without touching individual route handlers.
    """
    method = request.method
    path = request.url.path

    await AffordmedLogger(
        log_level="INFO",
        message=f"Received {method} request at {path}",
    )

    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        await AffordmedLogger(
            log_level="ERROR",
            message=f"Unhandled exception on {method} {path}: {type(exc).__name__}: {exc}",
        )
        raise


app.include_router(api_router)


@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok"}
