import asyncio
import httpx
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

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
    domian = "donga"
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

                        dong_a_id = urlparse(url).path.strip("/").split("/")[-2]

                        art_id = f"{domian}_{dong_a_id}"
                        art_name = soup_art.select_one('#contents > header > div > section > h1').text
                        art_content = soup_art.select_one('#contents > div.view_body > div > div.main_view > section.news_view').text
                        art_date = soup_art.select_one('#contents > header > div > section > ul > li:nth-child(2) > button > span:nth-child(1)').text
                        art_write = soup_art.select_one('#contents > header > div > section > ul > li:nth-child(1) > strong').text

                        
                        
                        art_list.append({"art_id":art_id,"art_name":art_name,"art_content":art_content,"art_date":art_date,"art_url":art_url,"art_write":art_write})
                        

    save_path = fr"C:\Users\M\Desktop\project\01_getdata\get_data\data\crawl\{now_kst}"

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(art_list, f, ensure_ascii=False)


if __name__ == "__main__":
    asyncio.run(search(1))