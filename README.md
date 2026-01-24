# TermChat LT 🟢

A terminal-style real-time chat application with AI assistant built with MQTT, featuring retro aesthetics and Lithuanian language support.

## Features

✨ **Real-time Chat** - Connect with users worldwide via MQTT protocol  
🤖 **AI Assistant** - TERMAI responds in Lithuanian using Zhipu GLM-4  
🎨 **Retro Terminal UI** - Green phosphor CRT-style interface with typewriter effects  
📻 **Radio Streaming** - Listen to online radio while chatting  
📱 **Progressive Web App** - Install as native app on mobile and desktop  
🌐 **No Installation Required** - Works in any modern web browser  
🇱🇹 **Lithuanian Language Support** - Native UI and AI responses in Lithuanian

## AI Assistant

**TERMAI** is the built-in AI assistant that responds to:
- Messages containing "ai" or "termai"
- Questions ending with "?"
- Responds in Lithuanian using Zhipu GLM-4 model
- Maintains conversation context

## Technical Architecture

### Frontend (index.html)
- Pure HTML5/CSS3/JavaScript
- MQTT WebSocket client (Paho)
- No external AI dependencies
- Sends messages, displays responses

### Backend (mqtt_service.py)
- Python MQTT service
- Zhipu GLM-4 AI integration
- Conversation memory
- Lithuanian language prompts

### Deployment
- Frontend: Static hosting (GitHub Pages, Netlify)
- Backend: Cloud service (Render, Heroku)
- MQTT: Public broker (broker.emqx.io)

## Setup & Configuration

### Environment Variables (.env)
```bash
ZHIPU_API_KEY=your-zhipu-api-key
AI_PROVIDER=zhipu
PORT=10000
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Start MQTT service
python mqtt_service.py

# Start web server
python -m http.server 8000
```

### Cloud Deployment
1. **Backend**: Deploy mqtt_service.py to Render/Heroku
2. **Frontend**: Deploy index.html to GitHub Pages/Netlify
3. **Environment**: Set ZHIPU_API_KEY in cloud service

## MQTT Configuration

- **Broker**: broker.emqx.io:1883 (Python) / :8084 (WebSocket)
- **Topic**: term-chat/global/v3
- **Protocol**: MQTT v5 (Python) / WebSocket (Browser)

## AI Integration

**Zhipu GLM-4 Model**:
- Lithuanian language optimization
- Conversation context awareness
- Trigger-based responses
- Error handling with fallbacks

**System Prompt**:
```
Tu esi TermAi, protingas asistentas TermChat LT kambaryje. 
Kalbėk lietuviškai trumpai ir aiškiai.
```
