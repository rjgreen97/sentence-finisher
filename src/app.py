from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


from src.main import finish_sentence

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class TextValues(BaseModel):
    sentence: str
    max_length: int


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})


@app.post("/finished_sentence", response_class=HTMLResponse)
async def finish(
    request: Request,
    sentence: str = Form(...),
    max_length: int = Form(...),
):
    result = finish_sentence(sentence, max_length)
    return templates.TemplateResponse(
        "finished_sentence.html",
        context={"request": request, "result": result},
    )
