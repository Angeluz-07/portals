from fastapi import FastAPI
from neo4j_init import init_driver
from config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD
from dao.PeopleDAO import get_actors_from_movie

app = FastAPI()

driver = init_driver(uri=NEO4J_URI,username=NEO4J_USERNAME,password=NEO4J_PASSWORD)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/actors")
async def actors():
    result = get_actors_from_movie(driver)
    return {"message": result}