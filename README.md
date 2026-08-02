# HealthQuest

A gamified health and wellbeing platform with an AI-powered health coach.

## Technology Stack

### Frontend
- **Framework**: React 18.3.1
- **Build Tool**: Vite 5.4.8
- **Styling**: Custom CSS with CSS variables
- **State Management**: React hooks

### Backend
- **Framework**: FastAPI 0.115.0
- **Server**: Uvicorn
- **Database**: PostgreSQL 16
- **Cache/Session**: Redis 7
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: bcrypt

### LLM Integration
- **RAG Framework**: LangChain
- **Vector Database**: ChromaDB
- **Embeddings**: fastembed (local)
- **LLM Providers**: 
  - Hugging Face (default)
  - Anthropic Claude
  - Google Gemini
  - Ollama (local)

## Project Structure

```
healthquest/
├── backend/           # Python FastAPI backend
├── frontend/          # React + Vite frontend
├── docs/              # Documentation
├── docker-compose.yml # Docker orchestration
└── README.md         # This file
```

## Quick Start

### Prerequisites
- Docker and Docker Compose
- (Optional) Python 3.12+ for local development

### Using Docker (Recommended)

```bash
# Start all services
docker compose up --build

# Access the application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Development

#### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Features

- **Gamified Health Tracking**: Daily quests, XP system, streaks, and badges
- **Health Coach AI**: RAG-powered assistant grounded in vetted health knowledge
- **Learning Modules**: Educational content with quizzes
- **Leaderboard**: Community engagement through XP rankings
- **Personalization**: Tailored recommendations based on health profile

## Documentation

- [Backend Documentation](backend/README.md)
- [Phase 2: AI Assistant](docs/PHASE2-ASSISTANT.md)
- [Phase 2: Gemini Integration](docs/PHASE2-GEMINI.md)
- [Phase 2: Ollama Integration](docs/PHASE2-OLLAMA.md)
- [Phase 3: Learning Features](docs/PHASE3-LEARNING.md)

## Environment Variables

See `.env.example` in the backend directory for required environment variables.

## License

This project is for educational purposes.
