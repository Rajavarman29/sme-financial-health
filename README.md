#  SME Financial Health Assessment Platform

> A full-stack web application that enables small and medium enterprises to assess their financial health through secure data ingestion, automated metric computation, and an interactive dashboard — no spreadsheet expertise required.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791.svg)
![React](https://img.shields.io/badge/Frontend-React-61DAFB.svg)
![Status](https://img.shields.io/badge/Status-Phase%201%20MVP-yellow.svg)

---

##  Problem Statement

SMEs rarely have dedicated finance teams. Owners rely on raw spreadsheets or gut instinct to evaluate their financial position — missing early warning signs of liquidity risk, over-leverage, or declining margins. This platform automates financial data ingestion, normalizes messy real-world data, and computes industry-standard KPIs through a secure, multi-user web application.

---

##  Key Features

-  **JWT Authentication** — Secure user registration and login with token-based auth
-  **CSV / XLSX Upload** — Upload raw financial statements directly from Excel or accounting exports
-  **Data Normalization Pipeline** — Cleans, standardizes, and structures uploaded financial data using pandas
-  **Data Encryption** — Sensitive financial records encrypted at rest using Fernet symmetric encryption
-  **Financial Metrics API** — Computes key ratios across 4 categories: liquidity, profitability, leverage, efficiency
-  **React Dashboard** — Interactive frontend for visualizing KPIs and financial trends *(in progress)*
-  **PostgreSQL Backend** — Relational data storage with proper multi-tenant schema design
-  **Auto API Docs** — Swagger UI available at `/docs` out of the box via FastAPI

---

##  Architecture

```
User (Browser)
     ↓
React Frontend  ──── Axios HTTP ────►  FastAPI Backend
                                            │
                              ┌─────────────┼─────────────┐
                              ↓             ↓             ↓
                         Auth Router   Upload Router  Metrics Router
                              │             │             │
                         JWT Token    pandas Parser  Metrics Engine
                                           │
                                    Fernet Encryption
                                           │
                                      PostgreSQL
```

### Project Structure

```
sme-financial-platform/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── database.py          # PostgreSQL connection & session
│   │   ├── routers/
│   │   │   ├── auth.py          # Login & registration
│   │   │   ├── upload.py        # CSV/XLSX ingestion
│   │   │   └── metrics.py       # Financial KPI endpoints
│   │   ├── models/              # SQLAlchemy ORM models
│   │   ├── schemas/             # Pydantic request/response schemas
│   │   └── services/
│   │       ├── parser.py        # Data normalization pipeline
│   │       ├── metrics.py       # Financial ratio computation
│   │       └── encryption.py    # Fernet encryption utilities
│   └── requirements.txt
│
└── frontend/                    # React app (in progress)
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   └── api/                 # Axios client
    └── package.json
```

---

##  Financial Metrics Computed

| Category | Metrics |
|---|---|
| **Liquidity** | Current Ratio, Quick Ratio |
| **Profitability** | Gross Margin, Net Profit Margin, Return on Equity |
| **Leverage** | Debt-to-Equity Ratio, Interest Coverage Ratio |
| **Efficiency** | Asset Turnover, Receivables Turnover |

---

##  Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+, JavaScript (ES6+) |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Data Processing | Pandas |
| Authentication | JWT (`python-jose`) |
| Encryption | `cryptography` (Fernet) |
| Frontend | React.js |
| HTTP Client | Axios |
| API Docs | Swagger UI (auto via FastAPI) |

---

##  How to Run

### Prerequisites
- Python 3.10+
- PostgreSQL running locally
- Node.js 18+ and npm

### Backend Setup

```bash
git clone https://github.com/rajavarman/sme-financial-platform.git
cd sme-financial-platform/backend

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env: DATABASE_URL, SECRET_KEY, ENCRYPTION_KEY

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

Swagger docs: `http://localhost:8000/docs`

### Frontend Setup *(in progress)*

```bash
cd ../frontend
npm install
npm start
```

Frontend: `http://localhost:3000`

---

##  API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | User registration |
| `POST` | `/auth/login` | JWT token generation |
| `POST` | `/upload` | Upload CSV/XLSX financial file |
| `GET` | `/metrics/{company_id}` | Retrieve computed KPIs |
| `GET` | `/health` | API health check |

---

##  Screenshots

| Login | Upload | KPI Dashboard |
|---|---|---|
| ![Login](screenshots/login.png) | ![Upload](screenshots/upload.png) | ![Dashboard](screenshots/dashboard.png) |

> _Add screenshots to `/screenshots` after running the app._

---

##  Build Status

| Module | Status |
|---|---|
| FastAPI Backend |  Complete |
| PostgreSQL Schema |  Complete |
| CSV/XLSX Parser |  Complete |
| Financial Metrics Engine |  Complete |
| JWT Authentication |  Complete |
| Data Encryption |  Complete |
| React Frontend |  In Progress |

---

##  Security

- Passwords hashed with bcrypt
- Financial data encrypted at rest (Fernet AES-128)
- All routes protected with JWT bearer tokens
- Environment variables for all secrets (never hardcoded)

---

##  Author

**Rajavarman M** — B.Tech AI & Data Science, Rajalakshmi Institute of Technology  
📧 rajavarman419@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/raja-varman-7b6063257/)
