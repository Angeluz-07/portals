from fastapi import FastAPI
from repository import TasksRepository, Task
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Handle CORS in local dev
origins= [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_methods=["*"],
)

# repository
repository = TasksRepository()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": repository.get_all()}


@app.post("/tasks")
def add_task(new_task: Task):
    repository.save(new_task)
    return {"message": repository.get_all()}
    

@app.post("/tasks/{id}/")
def update_task_status(id: int):
    item = repository.get_by_id(id)
    item.status = not (item.status)
    return {"task": item}