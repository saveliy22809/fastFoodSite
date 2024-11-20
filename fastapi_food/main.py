from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi_food.routes import clients, products

app = FastAPI()

# Подключаем шаблоны
templates = Jinja2Templates(directory="fastapi_food/templates")

# Подключаем маршруты
app.include_router(clients.router)
app.include_router(products.router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
