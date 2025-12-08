from fastapi import FastAPI
from scheduler import crawl_start
from dong_A_crawler import search

app = FastAPI()
sch = crawl_start()


@app.get('/')
async def start():
    sch.start()
    return None