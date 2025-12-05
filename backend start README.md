# TradeBerg V2 - Setup & Run Guide

This repository contains the full stack for the TradeBerg AI trading assistant.

-   **Backend**: FastAPI (Python) with LangChain, Gemini, and PostgreSQL (pgvector).
-   **Frontend**: Next.js (TypeScript) with Tailwind CSS.

---

## 1. Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.10+**
*   **Node.js 20+**
*   **PostgreSQL 17+** (Required for `pgvector` compatibility)
*   **Homebrew** (macOS)

### Install System Dependencies (macOS)

```bash
# 1. Install PostgreSQL 17
brew install postgresql@17
brew link postgresql@17 --force
brew services start postgresql@17

# 2. Install pgvector extension
brew install pgvector
```

---

## 2. Database Setup

You need to create the database user, the database itself, and enable the vector extension.

```bash
# 1. Create the 'postgres' superuser (if not exists)
createuser -s postgres

# 2. Create the 'tradeberg' database
createdb tradeberg

# 3. Enable the pgvector extension
psql -d tradeberg -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

---

## 3. Backend Setup

1.  **Navigate to backend:**
    ```bash
    cd backend
    ```

2.  **Create and activate virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in `backend/` with the following keys:
    ```env
    DATABASE_URL=postgresql://postgres@localhost:5432/tradeberg
    GEMINI_API_KEY=your_gemini_api_key
    # Add other keys as needed (e.g., SERPER_API_KEY)
    ```

---

## 4. Frontend Setup

1.  **Navigate to frontend:**
    ```bash
    cd frontend
    ```

2.  **Install Node dependencies:**
    ```bash
    npm install
    ```

3.  **Configure Environment Variables:**
    Create a `.env.local` file in `frontend/` (if not exists):
    ```env
    NEXT_PUBLIC_API_URL=http://127.0.0.1:8080/api
    ```

---

## 5. Running the Application

You need two terminal windows.

### Terminal 1: Backend
```bash
cd backend
source .venv/bin/activate
# Run on port 8080
python -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```
*Backend will be available at `http://localhost:8080`*

### Terminal 2: Frontend
```bash
cd frontend
# Run on port 3000
npm run dev
```
*Frontend will be available at `http://localhost:3000`*

---

## 6. Troubleshooting

### ❌ Error: `Address already in use` (Port 8080 or 3000)
If the server fails to start because the port is taken:

1.  **Find the process ID (PID):**
    ```bash
    lsof -i :8080  # For backend
    lsof -i :3000  # For frontend
    ```
2.  **Kill the process:**
    ```bash
    kill -9 <PID>
    ```

### ❌ Error: `role "postgres" does not exist`
Run this command to create the user:
```bash
createuser -s postgres
```

### ❌ Error: `type "vector" does not exist`
This means `pgvector` is not enabled. Run:
```bash
psql -d tradeberg -c "CREATE EXTENSION IF NOT EXISTS vector;"
```
*If this fails, ensure you installed `pgvector` via Homebrew.*

### ❌ Error: `could not open extension control file ... vector.control`
This happens if `pgvector` was installed for a different Postgres version.
**Fix:** Upgrade to Postgres 17 (see Prerequisites) and reinstall pgvector.

```bash
brew unlink postgresql@14
brew link postgresql@17 --force
brew reinstall pgvector
```
