# HealthQuest Project Restructure Plan

## Current Structure Issues
- Nested redundant folders: `vitala-backend/vitala-backend/` and `vitala-frontend/vitala-frontend/`
- Mixed configuration files at different levels
- Documentation scattered across backend folder
- No root-level coordination

## Proposed Professional Structure

```
healthquest/
├── backend/                          # Python FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── security.py
│   │   ├── serializers.py
│   │   ├── gamification.py
│   │   ├── game_data.py
│   │   ├── learn_data.py
│   │   ├── recommendations.py
│   │   ├── redis_client.py
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── profile.py
│   │   │   ├── quests.py
│   │   │   ├── leaderboard.py
│   │   │   ├── chat.py
│   │   │   └── learn.py
│   │   └── rag/
│   │       ├── assistant.py
│   │       ├── store.py
│   │       ├── embeddings.py
│   │       └── knowledge/
│   │           ├── hydration.md
│   │           ├── movement.md
│   │           ├── sleep.md
│   │           ├── nutrition.md
│   │           ├── stress.md
│   │           ├── hospital-info.md
│   │           └── using-healthquest.md
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   ├── .dockerignore
│   └── README.md
├── frontend/                         # React + Vite frontend
│   ├── src/
│   │   ├── main.jsx
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── styles.css
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── .gitignore
│   └── README.md
├── docs/                             # Documentation
│   ├── PHASE2-ASSISTANT.md
│   ├── PHASE2-GEMINI.md
│   ├── PHASE2-OLLAMA.md
│   ├── PHASE3-LEARNING.md
│   └── API.md
├── docker-compose.yml                # Root orchestration
├── .gitignore
└── README.md                         # Project overview
```

## Migration Steps

1. Create new directory structure
2. Move backend files from `vitala-backend/vitala-backend/` to `backend/`
3. Move frontend files from `vitala-frontend/vitala-frontend/` to `frontend/`
4. Move documentation to `docs/`
5. Update docker-compose.yml paths
6. Update any hardcoded paths in code
7. Update README files
8. Remove old nested directories
9. Test all services

## Benefits
- Clean, professional structure
- Clear separation of concerns
- Easier navigation and maintenance
- Better for version control
- Industry-standard layout
