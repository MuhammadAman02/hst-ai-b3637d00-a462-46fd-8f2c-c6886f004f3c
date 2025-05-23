from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

# Configure templates if the directory exists
templates_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
if os.path.exists(templates_dir):
    templates = Jinja2Templates(directory=templates_dir)

    @router.get("/", response_class=HTMLResponse)
    async def index(request: Request):
        """Render the index page."""
        return templates.TemplateResponse("index.html", {"request": request})
else:
    @router.get("/")
    async def index():
        """Redirect to NiceGUI app when using that framework."""
        return {"message": "This endpoint is not used when NiceGUI is active. Access the root URL directly."}