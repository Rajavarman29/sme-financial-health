# SME Financial Health Assessment Platform

This project is a Phase-1 MVP for assessing the financial health of SMEs.

## Tech Stack
- Backend: FastAPI (Python)
- Database: PostgreSQL
- Data Processing: pandas
- Frontend: React (in progress)

## Features
- User authentication
- CSV/XLSX financial data upload
- Data normalization & encryption
- Financial metrics calculation
- API documentation via Swagger

## How to Run Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app
