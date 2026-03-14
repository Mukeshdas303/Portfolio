# Mukesh — Animated Portfolio
> FastAPI + Three.js + GSAP + Typed.js

## Stack
| Layer | Tech |
|-------|------|
| Backend | FastAPI, Uvicorn, Pydantic |
| Frontend | HTML5, CSS3, Vanilla JS |
| 3D / Particles | Three.js (r128) |
| Scroll Animations | GSAP 3 + ScrollTrigger |
| Reveal Animations | AOS (Animate On Scroll) |
| Typewriter Effect | Typed.js |
| Data | JSON files (SQLite optional) |

## Project Structure
```
portfolio/
├── main.py               ← FastAPI app (routes + static)
├── requirements.txt
├── data/
│   └── portfolio.json    ← All content (about, skills, projects, timeline)
├── templates/
│   └── index.html        ← Single-page frontend (HTML + CSS + JS)
└── static/               ← (Place extra CSS/JS/images here)
    ├── css/
    ├── js/
    └── assets/
```

## API Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Serve portfolio SPA |
| GET | `/api/about` | Personal info & stats |
| GET | `/api/skills` | Skills with levels |
| GET | `/api/projects` | Project cards |
| GET | `/api/timeline` | Education + experience |
| POST | `/api/contact` | Contact form submission |
| GET | `/api/health` | Health check |

## Setup & Run

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
cd portfolio
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 4. Open your browser
# → http://localhost:8000
```

## Customise Content
Edit `data/portfolio.json` — no code changes needed:
- `about` → name, bio, taglines, stats
- `skills` → ai_ml / backend bars + tool chips
- `projects` → cards with tags, status, colour, icon
- `timeline` → education & project milestones

## Sections
1. **Hero** — Three.js particle network + GSAP entrance + Typed.js taglines
2. **About** — Bio, animated stats, rotating avatar border
3. **Skills** — Scroll-triggered progress bars (AI/ML + Backend)
4. **Projects** — 3-column card grid with hover glow effect
5. **Timeline** — Vertical journey with animated dot connectors
6. **Contact** — Info + live form posting to `/api/contact`

## Production Deployment
```bash
# Use Gunicorn + Uvicorn workers
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
