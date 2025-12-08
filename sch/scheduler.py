from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dong_A_crawler import search

def crawl_start():
    sch = AsyncIOScheduler()
    sch.add_job(search,'interval',minutes=30,id="search1", args=[1])
    return sch

