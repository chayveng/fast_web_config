from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.schemas.configure import Configure, ConfigureRequest
from app.services.config_service import ConfigService


templates_path = "./app/templates"
templates = Jinja2Templates(directory=templates_path)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/greeting")
def read_root():
    return {"Hello": "World"}


@app.get("/home")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/configure")
async def configure_form(request: Request):
    config_service = ConfigService()
    result: Configure = await config_service.current_config()
    return templates.TemplateResponse(
        "configure.html",
        {"request": request, "default": result},
    )


@app.post("/submit_config")
async def submit_config(configure: ConfigureRequest):
    config = configure.dict()
    config_service = ConfigService()
    # directory = "app/static/configure"
    create = await config_service.create_config_file(data=config)
    return {"message": "submit", "create": create}


@app.get("/submit")
async def success_page(request: Request):
    config_service = ConfigService()
    default: Configure = await config_service.current_config()
    return default

