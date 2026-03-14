from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json
import os




# ── Absolute paths ─────────────────────────────────────────────────────────────
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR    = os.path.join(BASE_DIR, "static")
DATA_PATH     = os.path.join(BASE_DIR, "data", "portfolio.json")

print(f"[Portfolio] BASE      : {BASE_DIR}")
print(f"[Portfolio] TEMPLATES : {TEMPLATES_DIR}  exists={os.path.isdir(TEMPLATES_DIR)}")
print(f"[Portfolio] STATIC    : {STATIC_DIR}     exists={os.path.isdir(STATIC_DIR)}")
print(f"[Portfolio] DATA      : {DATA_PATH}       exists={os.path.isfile(DATA_PATH)}")

os.makedirs(STATIC_DIR, exist_ok=True)

app = FastAPI(title="Mukesh Portfolio API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

port = int(os.environ.get("PORT", 10000))


def load_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

# ── Models ─────────────────────────────────────────────────────────────────────
class ContactMessage(BaseModel):
    name: str
    email: str
    subject: str
    message: str

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Serve the main portfolio SPA."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/about")
async def get_about():
    """Return personal info, bio, stats."""
    data = load_data()
    return data["about"]


@app.get("/api/skills")
async def get_skills():
    """Return all skill categories."""
    data = load_data()
    return data["skills"]


@app.get("/api/projects")
async def get_projects():
    """Return all projects."""
    data = load_data()
    return data["projects"]


@app.get("/api/timeline")
async def get_timeline():
    """Return education + experience timeline."""
    data = load_data()
    return data["timeline"]


@app.post("/api/contact")
async def send_contact(msg: ContactMessage):
    """Handle contact form submission.
    
    In production: integrate SMTP (smtplib / SendGrid) or save to DB.
    """
    # TODO: replace with real email / DB logic
    print(f"[Contact] From: {msg.name} <{msg.email}> | {msg.subject}")
    print(f"[Contact] Message: {msg.message}")
    return {
        "status": "success",
        "message": f"Thanks {msg.name}! I'll get back to you soon."
    }


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "Mukesh Portfolio API"}


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)