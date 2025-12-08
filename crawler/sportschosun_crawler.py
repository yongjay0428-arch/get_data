from bs4 import BeautifulSoup
# from util.logger import Logger
import httpx
import asyncio
# logger = Logger().get_logger(__name__)
URL = "https://www.sportschosun.com/latest/?action=all&"

async def search():
    print("구동 시작 ")
    i = 0 
    while True:
        async with httpx.AsyncClient() as client:
            param={"page":i}
            resp = await client.get(URL,params=param)

            soup = BeautifulSoup(resp.text,"html.parser")
            elem = soup.select("""
                    div.post-data >a.post-title
                            """)
            
            print(elem)
            # for e in elem:
            #     if e:
            #         art_name = e.select_one()
            #         art_content = e.select_one()
            #         art_date = e.select_one()
            #         art_pic = e.select_one()
            #         art_path = e.select_one()
            #         art_url = e.select_one()
            #         art_writer = e.select_one()
            # break

if __name__ == "__main__":
    asyncio.run(search())