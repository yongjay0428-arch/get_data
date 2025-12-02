from util.logger import Logger
import httpx
from bs4 import BeautifulSoup
import json
import asyncio


logger = Logger().get_lgger(__name__)
logger.info("logger 설정 완료")

async def search():
    # logger.info(f'keyword: {keyword}')
    url = 'https://www.bigkinds.or.kr/'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        elements = soup.select('''ul.today > li > div > a.issupop-btn''')
        logger.info(f'elements: {len(elements)}')
        issues = [ ]
        
        for elem in elements:
            # print(elem.get_text())
            issues.append(elem.get_text())
            print(elem.get_text())
    return issues

if __name__ == '__main__': # 파일의 실행 위치를 확인하여 직접적으로 실행되는 경우에만 호출되도록한다
    asyncio.run(search()) #비동기 함수인 search()를 호출하기 위해서 asyncio 이벤트 객체에 담아준다
                            #혹은 wait를 사용할 수도 있다

# 직접 실행에 대해서면 실행하도록 하는 이유는 구조상 파일이 호출될 때. 즉, import 될 때도 실행이 되는 상황이된다
# 이로 인한 부작용을 피하기 위해서 이런 방식으로 직접 호출 -> 실행의 구조를 선택해서 사용한다

