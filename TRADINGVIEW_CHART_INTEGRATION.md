# TradingView Chart Integration

## Overview
The TradeBerg platform now includes an integrated TradingView chart that appears alongside the chatbox, allowing users to analyze charts and interact with the AI assistant simultaneously.

## Features

### 1. **Split-Screen Layout**
- **Chart Section (Left 50%)**: Full TradingView chart with all features
- **Chat Section (Right 50%)**: AI chatbox for analysis and questions
- Responsive design that adapts to screen size

### 2. **Chart Screenshot Functionality**
- **Capture Button**: Blue button in top-right corner of chart
- **One-Click Screenshot**: Captures the entire chart view
- **Auto-Send to Chat**: Screenshot is automatically added to the chat
- **Download Option**: Screenshot is also downloaded to your device

### 3. **AI Chart Analysis**
When you capture a screenshot:
1. Click the "Capture Chart" button
2. The screenshot is automatically sent to the chatbox
3. The AI can analyze the chart image
4. Ask questions about patterns, trends, support/resistance levels

## How to Use

### Starting the Application

1. **Start Backend**:
   ```bash
   cd backend
   python -m uvicorn app:app --reload --host 0.0.0.0 --port 8080
   ```

2. **Start Frontend**:
   ```bash
   cd frontend
   npm run dev
   ```

3. **Access**: Open http://localhost:3000

### Using the Chart

1. **Navigate to a chat**: Click on any chat or create a new one
2. **View the chart**: TradingView chart appears on the left side
3. **Interact with chart**:
   - Zoom in/out
   - Change timeframes (1m, 5m, 15m, 1h, 4h, 1D, etc.)
   - Add indicators
   - Draw trendlines and patterns

### Capturing Screenshots

1. **Click "Capture Chart"** button (top-right of chart)
2. Wait for "Capturing..." to finish
3. Screenshot appears in chat automatically
4. Ask AI to analyze: "What do you see in this chart?"

## Example Interactions

### Chart Analysis
```
User: [Captures chart screenshot]
User: "Analyze this Bitcoin chart. What are the key support and resistance levels?"

AI: "Based on the chart:
- Strong support at $95,000
- Resistance at $118,000
- Currently in a consolidation phase
- Volume declining, suggesting potential breakout soon"
```

### Pattern Recognition
```
User: [Captures chart screenshot]
User: "Do you see any chart patterns forming?"

AI: "I can see a potential:
- Head and Shoulders pattern forming
- Neckline around $100,000
- If broken, target would be $85,000
- Watch for volume confirmation"
```

### Trading Decisions
```
User: [Captures chart screenshot]
User: "Should I enter a long position here?"

AI: "Analysis:
- Price is at key support
- RSI showing oversold conditions
- Volume increasing on bounces
- Risk/Reward: Good entry point
- Stop loss: Below $94,000
- Target: $110,000"
```

## Technical Details

### Components

1. **TradingViewChart.tsx**
   - Location: `frontend/src/components/chart/TradingViewChart.tsx`
   - Uses TradingView widget API
   - Implements html2canvas for screenshots
   - Dark theme by default

2. **Chat Page Layout**
   - Location: `frontend/src/app/(main)/c/[chatId]/page.tsx`
   - Split-screen flex layout
   - Responsive design
   - Screenshot integration

### Dependencies

- **TradingView Widget**: Loaded from CDN
- **html2canvas**: For screenshot capture
- **Next.js Dynamic Import**: For client-side only rendering

### Configuration

The chart can be customized in `TradingViewChart.tsx`:

```typescript
// Change default symbol
symbol: "BTCUSD"  // or "ETHUSD", "SOLUSD", etc.

// Change default timeframe
interval: "15"  // 1, 5, 15, 60, 240, D, W, M

// Change theme
theme: "dark"  // or "light"
```

## Troubleshooting

### Chart Not Loading
- Check internet connection (TradingView loads from CDN)
- Verify browser allows third-party scripts
- Clear browser cache and reload

### Screenshot Not Working
- Ensure html2canvas is installed: `npm install html2canvas`
- Check browser console for errors
- Try different browser (Chrome/Edge recommended)

### Layout Issues
- Ensure screen width is at least 1024px
- Try zooming out if chart is cut off
- Check responsive breakpoints in CSS

## Future Enhancements

- [ ] Multiple chart layouts (1, 2, 4 charts)
- [ ] Symbol selector in UI
- [ ] Timeframe quick-select buttons
- [ ] Chart templates (save/load configurations)
- [ ] Drawing tools sync with AI
- [ ] Real-time price alerts
- [ ] Chart sharing with other users

## Support

For issues or questions:
1. Check backend logs for API errors
2. Check browser console for frontend errors
3. Verify all dependencies are installed
4. Ensure backend is running on port 8080
5. Ensure frontend is running on port 3000

---

**Note**: The TradingView chart requires an active internet connection to load market data. The screenshot feature works offline once the chart is loaded.
