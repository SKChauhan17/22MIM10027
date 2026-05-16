# Campus Notifications & Vehicle Maintenance Scheduler API

A high-performance, production-grade REST API built with FastAPI for managing campus-wide notifications and scheduling preventive vehicle maintenance workflows.

## Overview

This service acts as the central backend for delivering real-time campus notifications and coordinating vehicle maintenance schedules. It is designed for reliability, observability, and horizontal scalability.

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11+ |
| Validation | Pydantic v2 |
| HTTP Client | HTTPX (async) |
| Server | Uvicorn (ASGI) |

## Project Structure

```
.
├── app/
│   ├── api/         # Route handlers and endpoint definitions
│   ├── core/        # Cross-cutting concerns (logging, config, security)
│   ├── models/      # Pydantic data models and schemas
│   └── services/    # Business logic and external integrations
├── main.py          # Application entry point
├── requirements.txt
└── .gitignore
```

## Setup & Installation

**Prerequisites:** Python 3.11+

```bash
# 1. Clone the repository
git clone <repository-url>
cd <project-directory>

# 2. Create and activate the virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your values

# 5. Start the development server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive documentation is at `http://localhost:8000/docs`.

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `LOGGING_URL` | Endpoint for the centralized logging service | `https://test-server-endpoint.com/log` |

## API Reference

Interactive Swagger UI documentation is auto-generated and available at `/docs` when the server is running.
