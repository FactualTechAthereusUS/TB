# Perplexity API Chatbox Integration Guide

## ✅ Integration Status: FULLY CONFIGURED

Your TradeBerg chatbox is now properly integrated with Perplexity API for professional trading analysis.

---

## 🎯 What Was Configured

### 1. **Perplexity Service** (`backend/perplexity_bot/services/perplexity_service.py`)
- ✅ Full Perplexity API integration
- ✅ Professional trading prompt enhancement
- ✅ Citation and source extraction
- ✅ Related questions generation
- ✅ Conversation history management
- ✅ Error handling and fallbacks

### 2. **Chat Service Priority** (`backend/services/chat_service.py`)
- ✅ **Priority 1:** Perplexity API (best for trading)
- ✅ **Priority 2:** OpenAI GPT-4o (fallback)
- ✅ **Priority 3:** Intelligent fallback responses
- ✅ Streaming support for real-time responses
- ✅ Citations and related questions in responses

### 3. **API Configuration** (`backend/.env`)
```env
PERPLEXITY_API_KEY=pplx-YOUR_API_KEY_HERE
OPENAI_API_KEY=sk-proj-...
```

---

## 🔄 How It Works

### Request Flow

```
User types in chatbox
        ↓
Frontend: POST /api/chat/[chatId]/message
        ↓
Next.js API Route (proxy)
        ↓
Backend: POST /api/chat/{chatId}/stream
        ↓
Chat Service: stream_response()
        ↓
Priority 1: Try Perplexity API
    ├─ Success → Stream response with citations
    └─ Fail → Try OpenAI
        ├─ Success → Stream OpenAI response
        └─ Fail → Use fallback response
```

### Perplexity Enhancement

When a user sends a message, the system:

1. **Detects Query Type:**
   - Chart analysis
   - Position check
   - Market research
   - Price check

2. **Enhances Prompt:**
   - Adds institutional trading context
   - Focuses on liquidity and order flow
   - Requests specific price levels
   - Avoids retail indicators

3. **Calls Perplexity API:**
   - Model: `sonar-pro`
   - Temperature: 0.2 (focused)
   - Max tokens: 4000
   - Returns citations and related questions

4. **Formats Response:**
   - Main analysis content
   - Source citations (top 3)
   - Related questions (top 3)
   - Streams word-by-word for UX

---

## 📊 Response Format

### Example User Message:
```
"What's the current Bitcoin price and market sentiment?"
```

### Perplexity Enhanced Prompt:
```
As a market analyst, provide current market analysis for: What's the current Bitcoin price and market sentiment?

Include:
1. Current Price Action: Real-time analysis and immediate context
2. Key Levels: Support, resistance, and critical price zones
3. Market Sentiment: Current positioning and sentiment indicators
4. Short-term Outlook: Immediate scenarios and probability assessments
5. Trading Opportunities: Potential setups with specific levels

Focus on actionable information with clear price targets and timeframes.
```

### Response to User:
```markdown
## Bitcoin Market Analysis

**Current Price Action:**
Bitcoin is trading at $43,250, showing consolidation after recent volatility...

**Key Levels:**
- Support: $42,000 (strong liquidity zone)
- Resistance: $44,500 (previous high)
- Critical: $41,000 (major support)

**Market Sentiment:**
Current sentiment is cautiously bullish with...

**Sources:**
1. [CoinDesk - Bitcoin Price](https://coindesk.com/...)
2. [CryptoQuant - On-chain Data](https://cryptoquant.com/...)
3. [Glassnode - Market Sentiment](https://glassnode.com/...)

**Related Questions:**
- What are the key support levels for Bitcoin?
- How does Bitcoin's current price compare to historical trends?
- What factors are influencing Bitcoin's price movement?
```

---

## 🧪 Testing the Integration

### Option 1: Run Test Script

```bash
cd backend
python test_perplexity_connection.py
```

Expected output:
```
✅ PASS - Configuration
✅ PASS - Service Import
✅ PASS - API Call
✅ PASS - Chat Integration
✅ PASS - Backend Config

Results: 5/5 tests passed
🎉 ALL TESTS PASSED!
```

### Option 2: Manual Test

1. **Start Backend:**
```bash
cd backend
python -m uvicorn app:app --reload --port 8080
```

2. **Start Frontend:**
```bash
cd frontend
npm run dev
```

3. **Test in Browser:**
   - Go to `http://localhost:3000`
   - Type: "Analyze Bitcoin market"
   - Watch for streaming response with citations

4. **Check Backend Logs:**
```
🔵 Using Perplexity API for trading analysis
✅ Perplexity response completed (1234 tokens)
```

---

## 🎨 Features in Chatbox

### 1. **Professional Trading Analysis**
- Institutional-grade market insights
- Liquidity and order flow analysis
- Specific price levels and targets
- Risk-reward scenarios

### 2. **Real-time Streaming**
- Word-by-word streaming for better UX
- Smooth 20ms delay between words
- No waiting for full response

### 3. **Source Citations**
- Top 3 sources automatically included
- Clickable links to original articles
- Builds trust and credibility

### 4. **Related Questions**
- AI-generated follow-up questions
- Helps users explore topics deeper
- Guides conversation flow

### 5. **Conversation History**
- Last 10 messages preserved
- Context-aware responses
- Multi-turn conversations

---

## 🔧 Configuration Options

### Perplexity Model Selection

Edit `backend/perplexity_bot/config.py`:

```python
# Available models:
DEFAULT_MODEL = "sonar-pro"  # Best for trading (current)
# DEFAULT_MODEL = "sonar"    # Faster, cheaper
# DEFAULT_MODEL = "sonar-reasoning"  # Deep analysis
```

### Response Length

```python
MAX_TOKENS = 4000  # Current setting
# MAX_TOKENS = 2000  # Shorter responses
# MAX_TOKENS = 8000  # Longer, detailed analysis
```

### Temperature (Creativity)

```python
TEMPERATURE = 0.2  # Current (focused, factual)
# TEMPERATURE = 0.5  # More creative
# TEMPERATURE = 0.0  # Most deterministic
```

---

## 📈 API Priority Logic

### Why Perplexity First?

1. **Real-time Data:** Perplexity has access to current market data
2. **Citations:** Provides sources for credibility
3. **Trading Focus:** Better for financial analysis
4. **Related Questions:** Helps user engagement

### When OpenAI is Used

- Perplexity API is down
- Perplexity rate limit hit
- Perplexity API key invalid
- Network issues with Perplexity

### Fallback Response

- Both APIs unavailable
- Provides helpful context-aware message
- Suggests checking API configuration
- Maintains user experience

---

## 🐛 Troubleshooting

### Issue: "Perplexity service error"

**Check:**
1. API key in `backend/.env`:
   ```env
   PERPLEXITY_API_KEY=pplx-...
   ```
2. Run test: `python test_perplexity_connection.py`
3. Check backend logs for detailed error

**Solution:**
```bash
# Verify API key
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('PERPLEXITY_API_KEY'))"
```

### Issue: No citations in response

**Cause:** Perplexity didn't return citations for this query

**Normal:** Not all queries have citations (e.g., general questions)

**Expected:** Market data queries usually have citations

### Issue: Slow responses

**Check:**
1. Perplexity API status
2. Network connection
3. Backend logs for processing time

**Optimize:**
```python
# Reduce max tokens
MAX_TOKENS = 2000

# Increase temperature for faster responses
TEMPERATURE = 0.5
```

### Issue: Rate limit errors

**Symptom:** "Rate limit exceeded" in logs

**Solution:**
1. Perplexity has rate limits (check your plan)
2. System will auto-fallback to OpenAI
3. Consider upgrading Perplexity plan

---

## 📊 Monitoring

### Backend Logs

Watch for these indicators:

```bash
# Success
🔵 Using Perplexity API for trading analysis
✅ Perplexity response completed (1234 tokens)

# Fallback
❌ Perplexity service error: ...
⚠️ Falling back to OpenAI
🟢 Using OpenAI API as fallback
✅ OpenAI response completed

# Full fallback
⚠️ All AI services unavailable, using fallback
```

### Response Quality

Good indicators:
- ✅ Specific price levels mentioned
- ✅ Citations included
- ✅ Related questions provided
- ✅ Professional terminology used
- ✅ Response < 5 seconds

---

## 🎯 Best Practices

### 1. **User Prompts**

Good:
- "Analyze Bitcoin price action"
- "What's the current sentiment for @AAPL?"
- "Show me key support levels for ETH"

Better:
- "Analyze Bitcoin price action with key liquidity zones"
- "What's the institutional sentiment for Apple stock?"
- "Identify support and resistance levels for Ethereum with entry points"

### 2. **Conversation Flow**

- Use related questions to guide users
- Maintain context across messages
- Ask follow-up questions

### 3. **Error Handling**

- Always have fallback responses
- Log errors for debugging
- Provide helpful error messages to users

---

## 📚 API Documentation

### Perplexity API

- **Docs:** https://docs.perplexity.ai/
- **Models:** https://docs.perplexity.ai/docs/model-cards
- **Pricing:** https://docs.perplexity.ai/docs/pricing

### Your Integration

- **Service:** `backend/perplexity_bot/services/perplexity_service.py`
- **Config:** `backend/perplexity_bot/config.py`
- **Chat Service:** `backend/services/chat_service.py`
- **Test:** `backend/test_perplexity_connection.py`

---

## ✅ Verification Checklist

- [ ] Perplexity API key in `backend/.env`
- [ ] Test script passes all 5 tests
- [ ] Backend starts without errors
- [ ] Frontend connects to backend
- [ ] Chat creates successfully
- [ ] Messages stream properly
- [ ] Citations appear in responses
- [ ] Related questions show up
- [ ] Fallback works when APIs fail
- [ ] Backend logs show Perplexity usage

---

## 🎉 Success Indicators

When everything is working:

1. **Backend logs show:**
   ```
   🔵 Using Perplexity API for trading analysis
   ✅ Perplexity response completed (1234 tokens)
   ```

2. **Frontend displays:**
   - Streaming response (word by word)
   - Professional trading analysis
   - Source citations at bottom
   - Related questions section

3. **User experience:**
   - Fast response (2-5 seconds)
   - Relevant market data
   - Actionable insights
   - Professional quality

---

## 📞 Support

If issues persist:

1. Run: `python backend/test_perplexity_connection.py`
2. Check backend logs
3. Verify API keys
4. Test with simple query: "What is Bitcoin?"
5. Check Perplexity API status

---

**Status:** ✅ PERPLEXITY API FULLY INTEGRATED WITH CHATBOX

**Last Updated:** 2024-01-16

**Version:** 1.0.0
