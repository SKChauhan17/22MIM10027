# Campus Microservices Platform

An enterprise-grade, high-throughput microservices backend engineered with **Python** and **FastAPI** to deliver robust telemetry tracking, automated notification lifecycle processing, and industrial fleet vehicle coordination across distributed campus infrastructure.

---

## 🏗️ Architectural Topology

```
                         ┌─────────────────────────────────────────┐
                         │           ASGI Server (Uvicorn)         │
                         └──────────────────┬──────────────────────┘
                                            │
                         ┌──────────────────▼──────────────────────┐
                         │        CORSMiddleware  (Layer 1)        │
                         │  Preflight orchestration & origin guard │
                         └──────────────────┬──────────────────────┘
                                            │
                         ┌──────────────────▼──────────────────────┐
                         │   Request Logging Middleware (Layer 2)  │
                         │   Fire-and-forget telemetry via httpx   │
                         │      AffordmedLogger ──► POST /log      │
                         └──────────────────┬──────────────────────┘
                                            │
                    ┌───────────────────────▼────────────────────────┐
                    │              FastAPI Router  /api              │
                    │  ┌────────────┐ ┌─────────────┐ ┌───────────┐  │
                    │  │GET /depots │ │GET /vehicles│ │GET /notifs│  │
                    │  └────────────┘ └─────────────┘ └───────────┘  │
                    │              Pydantic Validation Layer         │
                    └────────────────────────────────────────────────┘
                                            │
                    ┌───────────────────────▼────────────────────────┐
                    │           Global Exception Handlers            │
                    │   RequestValidationError → 400 Bad Request     │
                    │   Exception              → 500 Internal Error  │
                    └────────────────────────────────────────────────┘
```

### Design Pillars

| Pillar | Implementation |
|--------|---------------|
| **Asynchronous Telemetry Proxy** | Every ingress request triggers a fire-and-forget `httpx` coroutine shipping a structured log event out-of-band — zero latency added to the response path |
| **Decoupled Validation Domain** | Pydantic v2 boundaries trap malformed payloads at the network perimeter; native FastAPI 422 schemas are overridden with a unified `{ error, details[] }` contract |
| **Cross-Origin Pipeline Isolation** | Full CORS preflight orchestration via `CORSMiddleware` positioned as the outermost application layer |
| **Paginated Data Contracts** | Notification endpoints expose `{ total, page, limit, results[] }` envelopes enabling stateless frontend pagination |

---

## 📁 Project Structure

```
.
├── main.py                        # ASGI entry point; middleware & router registration
├── requirements.txt
└── app/
    ├── api/
    │   └── routers.py             # /api route handlers
    ├── core/
    │   ├── exceptions.py          # Global error handlers (400 / 500)
    │   ├── logger.py              # AffordmedLogger async telemetry utility
    │   └── mock_data.py           # In-memory seed data (depots, vehicles, notifications)
    ├── models/
    │   └── schemas.py             # Pydantic domain schemas
    └── services/                  # Business logic layer (Phase 4+)
```

---

## ⚙️ Configuration & Secrets Management

System parameters are externalized via environment variables. Create a `.env` file in the project root (never commit this file):

```env
# Telemetry endpoint — overrides the built-in fallback
LOGGING_URL=https://test-server-endpoint.com/log

# Base URL for the external evaluation service
EVALUATION_SERVICE_URL=http://4.224.186.213/evaluation-service

# Bearer token used for two independent purposes:
#   1. Authorization header on outbound telemetry log events
#   2. Authenticated proxy calls to EVALUATION_SERVICE_URL for
#      GET /api/depots and GET /api/vehicles
# When absent, both paths fall back to safe local behaviour —
# no live data is fetched and no Authorization header is sent.
ACCESS_CODE=<your_access_code>
```

> `ACCESS_CODE` is strictly optional. When absent, `/api/depots` and `/api/vehicles` serve the local mock dataset and telemetry requests omit the `Authorization` header entirely.

---

## 🛠️ Installation & Local Runtime

**Prerequisites:** Python 3.11+

```bash
# 1. Clone and enter the repository
git clone <repository-url>
cd <project-directory>

# 2. Create and activate the virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install all runtime dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env

# 5. Boot the ASGI development server
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

## 📊 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Liveness probe — returns `{"status": "ok"}` |
| `GET` | `/api/depots` | Full depot inventory |
| `GET` | `/api/vehicles` | Full vehicle fleet registry |
| `GET` | `/api/notifications` | Paginated, filterable notification feed |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc documentation interface |

### Notification Query Parameters

| Parameter | Type | Default | Constraints | Description |
|-----------|------|---------|-------------|-------------|
| `limit` | `int` | `10` | `1 ≤ x ≤ 50` | Results per page |
| `page` | `int` | `1` | `≥ 1` | 1-based page index |
| `notification_type` | `str` | `null` | `Alert \| Info \| Warning` | Case-insensitive type filter |

**Filtered, paginated request:**
```bash
curl "http://127.0.0.1:8000/api/notifications?notification_type=Alert&limit=5&page=1"
```

**Response envelope:**
```json
{
  "total": 8,
  "page": 1,
  "limit": 5,
  "results": [ "..." ]
}
```

---

## 🔒 Error Contract

All error responses conform to a uniform schema — no internal stack traces are exposed to clients.

**400 Bad Request** (validation failure):
```json
{
  "error": "Validation Failed",
  "details": [
    { "field": "query.limit", "message": "Input should be less than or equal to 50" }
  ]
}
```

**500 Internal Server Error:**
```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred."
}
```

Perimeter validation test:
```bash
curl "http://127.0.0.1:8000/api/notifications?limit=abc"
```

---

## 🧰 Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Language | Python | 3.11+ |
| Web Framework | FastAPI | ≥ 0.111 |
| Data Validation | Pydantic | v2 |
| Async HTTP Client | HTTPX | ≥ 0.27 |
| ASGI Server | Uvicorn | ≥ 0.29 |

---

## 🤝 Contributing

1. Branch from `main` using `feat/<scope>` or `fix/<scope>` naming.
2. Follow [Conventional Commits](https://www.conventionalcommits.org/) for all commit messages.
3. Pydantic models must remain strictly typed — no `Any` fields in domain schemas.
4. Verify `/docs` renders cleanly before opening a pull request.

---

## 📸 Execution Verification Matrix

### 1. Core Inventory Endpoints (`GET /api/depots` & `GET /api/vehicles`)

The endpoints resolve the target inventory datasets dynamically using a robust authenticated reverse proxy layer, safely maintaining local dataset fallbacks for high-availability execution.

![Depots Matrix](assets/Screenshot%20(189).png)
![Vehicles Inventory](assets/Screenshot%20(192).png)

### 2. Notifications Pagination & Type Filtering Gateway

Demonstrates automated parameter slicing arrays dynamically based on limit and page index scopes alongside case-insensitive matching filters.

![Pagination & Filtering Rules](assets/Screenshot%20(196).png)

### 3. Perimeter Validation Injection Testing (`limit=abc`)

Demonstrates our custom validation exception router catching runtime data mismatches at the gate and uniformizing default 422 processing states into clean HTTP 400 Bad Request contracts.

![Validation Perimeter Control](assets/Screenshot%20(201).png)
