# TradeBerg Frontend-Backend Connection Guide

## Overview
This guide explains how the React/Next.js frontend is connected to the FastAPI backend.

## Architecture

### Frontend (Next.js)
- **Location**: `frontend/`
- **Port**: 3000 (default)
- **Framework**: Next.js 15 with React 19

### Backend (FastAPI)
- **Location**: `backend/`
- **Port**: 8080 (default)
- **Framework**: FastAPI with SQLAlchemy

## Connection Method

The frontend connects to the backend through **Next.js API Routes** that act as proxies. All frontend API calls go through these routes, which then forward requests to the FastAPI backend.

### API Route Structure

```
Frontend Component
    ↓
Next.js API Route (/api/chat/*)
    ↓
FastAPI Backend (http://localhost:8080/api/chat/*)
```

## Setup Instructions

### 1. Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment (if not exists):
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create `.env` file in `backend/` directory:
```env
HOST=0.0.0.0
PORT=8080
DEBUG=True
ENVIRONMENT=development

CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# API Keys (optional for basic functionality)
PERPLEXITY_API_KEY=your_perplexity_api_key_here

DATABASE_URL=sqlite:///./data/tradeberg.db
```

6. Start backend server:
```bash
python app.py
# OR
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

### 2. Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env.local` file in `frontend/` directory:
```env
NEXT_PUBLIC_API_URL=http://localhost:8080/api
```

4. Start frontend development server:
```bash
npm run dev
```

## API Endpoints Mapping

### Chat Endpoints

| Frontend Route | Backend Route | Method | Description |
|---------------|---------------|--------|-------------|
| `/api/chat` | `/api/chat` | GET | Get all chats |
| `/api/chat/create` | `/api/chat/create` | POST | Create new chat |
| `/api/chat/[chatId]` | `/api/chat/{chat_id}` | GET | Get chat by ID |
| `/api/chat/[chatId]/message` | `/api/chat/{chat_id}/messages` | GET | Get messages |
| `/api/chat/[chatId]/message` | `/api/chat/{chat_id}/stream` | POST | Stream AI response |
| `/api/chat/limit` | `/api/chat/limit` | GET | Get token limit |

### Trading Endpoints

| Frontend Route | Backend Route | Method | Description |
|---------------|---------------|--------|-------------|
| `/api/trading/history` | `/api/trading/history` | GET | Get trading history |
| `/api/trading/zones` | `/api/trading/zones` | GET | Get zone history |

## Database

The backend uses SQLite by default. Database file location: `backend/data/tradeberg.db`

### Tables
- `chats` - Stores chat conversations
- `messages` - Stores individual messages
- `users` - Stores user information (for future use)

## Features

### ✅ Implemented
- Chat creation and listing
- Message storage and retrieval
- Streaming AI responses
- Chat title auto-generation
- Trading history endpoints (mock data)
- Zone history endpoints (mock data)

### 🔄 To Be Implemented
- Real trading history storage
- Zone detection algorithm
- User authentication
- Token usage tracking
- Image upload for chart analysis

## Troubleshooting

### Backend not connecting
1. Check if backend is running on port 8080
2. Verify CORS settings in `backend/config.py`
3. Check backend logs for errors

### Frontend API errors
1. Verify `NEXT_PUBLIC_API_URL` in `.env.local`
2. Check browser console for CORS errors
3. Ensure Next.js API routes are working

### Database errors
1. Ensure `backend/data/` directory exists
2. Check database file permissions
3. Verify SQLAlchemy models are imported correctly

## Development Notes

- Backend runs on port 8080
- Frontend runs on port 3000
- API routes proxy requests to backend
- Streaming responses are forwarded directly
- Database auto-initializes on first run

