# Backend-Frontend Connection Test

## Quick Test Steps

### 1. Start Backend (Terminal 1)
```bash
cd backend
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8080
```

Wait for:
```
✅ Database initialized
🌐 CORS Origins: ['http://localhost:3000', ...]
INFO:     Uvicorn running on http://0.0.0.0:8080
```

### 2. Start Frontend (Terminal 2)
```bash
cd frontend
npm run dev
```

Wait for:
```
✓ Ready in 2.5s
○ Local:   http://localhost:3000
```

### 3. Test Backend Health
Open: `http://localhost:8080/health`

Expected:
```json
{
  "status": "healthy",
  "service": "TradeBerg API"
}
```

### 4. Test Frontend
Open: `http://localhost:3000`

Expected:
- ✅ Page loads
- ✅ No console errors
- ✅ Beautiful UI visible

### 5. Test Chat Connection
1. Type: "Hello"
2. Press Enter
3. Expected:
   - ✅ User message appears
   - ✅ AI response streams
   - ✅ No errors

## Success Indicators

✅ Backend running on port 8080
✅ Frontend running on port 3000
✅ No CORS errors in console
✅ Chat creates successfully
✅ AI responses stream properly
✅ Layout unchanged

## If Something Fails

### Backend won't start
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8080
```

### Frontend won't start
```bash
cd frontend
npm install
npm run dev
```

### CORS errors
Check `backend/.env`:
```
CORS_ORIGINS=http://localhost:3000
```

### Connection refused
1. Verify backend is running
2. Check `frontend/.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8080/api
```

## API Endpoints to Test

1. **Health Check**
   - URL: `http://localhost:8080/health`
   - Method: GET
   - Expected: `{ "status": "healthy" }`

2. **Get Chats**
   - URL: `http://localhost:8080/api/chat`
   - Method: GET
   - Expected: `[]` (empty array initially)

3. **Create Chat**
   - URL: `http://localhost:8080/api/chat/create`
   - Method: POST
   - Body: `{ "prompt": "Hello" }`
   - Expected: `{ "chatId": "..." }`

## Browser Console Check

Open DevTools (F12) → Console

Good signs:
```
✅ No red errors
✅ Successful fetch to localhost:8080
✅ Status 200 responses
```

Bad signs:
```
❌ CORS policy blocked
❌ Failed to fetch
❌ 404 Not Found
```

## Connection Status

If all tests pass:
🎉 **FULLY CONNECTED AND WORKING**

If any test fails:
📋 Check the troubleshooting section in `BACKEND_FRONTEND_CONNECTION_GUIDE.md`
