from sqlmodel import SQLModel, Field, select, Session, create_engine
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager


sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True)

templates = Jinja2Templates(directory="templates")

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    completed: bool = False

@asynccontextmanager
async def lifespan(app):
    #SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Address Search API",
    description="API for searching addresses using Elasticsearch with comparison capabilities",
    version="1.0.0",
    lifespan=lifespan,
)


def get_session():
    with Session(engine) as session:
        yield session

@app.get("/", response_class=HTMLResponse)
def index(request: Request, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.get("/toggle/{task_id}", response_class=HTMLResponse)
def toggle(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    task.completed = not task.completed
    session.add(task)
    session.commit()
    return templates.TemplateResponse("task.html", {"task": task})

from fastapi import Form

@app.post("/tasks", response_class=HTMLResponse)
def create_task(
    request: Request,
    title: str = Form(...),
    session: Session = Depends(get_session)
):
    task = Task(title=title)
    session.add(task)
    session.commit()
    session.refresh(task)
    return templates.TemplateResponse("task.html", {"request": request, "task": task})

def main():
    import uvicorn, os
    # cd to c:\learn\scratches
    os.chdir(r"c:\learn\scratches")
    uvicorn.run(
        "fastapi_htmx:app",
        host="localhost",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()