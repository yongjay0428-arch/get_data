import asyncio
import csv
import httpx
from bs4 import BeautifulSoup
from util.logger import Logger

logger = Logger().get_logger(__name__)
cat_dict = {
"Politics":"정치",
    "Economy":"경제",
    "Inter":"국제(세계)",
    "Society":"사회",
    "Entertainment":"생활/문화",
    "Sports":"스포츠"
}
async def search():
    logger.info("구동시작")
    cat_list = ["Politics","Economy","Inter","Society","Entertainment","Sports"]
    url = "https://www.donga.com/news/"
    art_list = []
    async with httpx.AsyncClient() as client:
        for cat in cat_list:
            for i in range(0,10):
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
                        art_list.append(
                                {
                                "art_cat":cat_dict[cat],
                                "art_title": e.select_one('article > div.news_body > h4.tit').text,
                                "art_desc":e.select_one('article > div.news_body > p.desc').text,
                                "art_url":e.select_one('article > div.news_body > h4.tit > a')['href']
                                }
                        )
    save_path = 'data/crawl/crawler_data.csv'
    with open(save_path,'w',encoding='utf-8-sig',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=art_list[0].keys())
        writer.writeheader()
        writer.writerows(art_list)

if __name__ == "__main__":
    asyncio.run(search())