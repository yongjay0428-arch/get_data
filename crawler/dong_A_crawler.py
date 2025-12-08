import asyncio
import csv
import httpx
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

# from util.logger import Logger

# logger = Logger().get_logger(__name__)

KST = timezone(timedelta(hours=9))
now_kst = datetime.now(KST).strftime("%Y%m%d_%H%M%S")

cat_dict = {
"Politics":"정치",
    "Economy":"경제",
    "Inter":"국제(세계)",
    "Society":"사회",
    "Entertainment":"생활/문화",
    "Sports":"스포츠"
}
async def search(i):
    print(f"구동시작:{now_kst}")
    cat_list = ["Politics","Economy","Inter","Society","Entertainment","Sports"]
    url = "https://www.donga.com/news/"
    art_list = []
    async with httpx.AsyncClient() as client:
        for cat in cat_list:
            for i in range(0,i):
                url = f"https://www.donga.com/news/{cat}"
                param = {'p':1+10*i}
                resp = await client.get(url,params=param)
                soup = BeautifulSoup(resp.text,"html.parser")

                elem = soup.select("""
                #contents > div > div > div > section > ul.row_list > li
                """)
                for e in elem:
                    # print(e)
                    if e:
                        art_url = e.select_one('article > div.news_body > h4.tit > a')['href']
                        resp_art = await client.get(url=art_url)
                        soup_art = BeautifulSoup(resp_art.text , "html.parser")

                        art_name = soup_art.select_one('#contents > header > div > section > h1')
                        art_content = soup_art.select_one('#contents > div.view_body > div > div.main_view > section.news_view')
                        art_date = soup_art.select_one('#contents > header > div > section > ul > li:nth-child(2) > button > span:nth-child(1)')
                        art_write = soup_art.select_one('#contents > header > div > section > ul > li:nth-child(1) > strong')

                        art_list.append({"art_name":art_name.text,"art_content":art_content.text,"art_date":art_date,"art_url":art_url,"art_write":art_write.text})

    save_path = f'data/crawl/dong_a_{now_kst}.csv'
    with open(save_path,'w',encoding='utf-8-sig',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=art_list[0].keys())
        writer.writeheader()
        writer.writerows(art_list)

if __name__ == "__main__":
    asyncio.run(search(2))