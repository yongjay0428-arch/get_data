import joblib
import pandas as pd
import re
import pandas as pd
import numpy as np

file_path = r"D:\STUDY\project\get_data\data\crawl\crawler_data.csv"

pd.set_option("display.max_rows", None)       # 행 생략 없이 모두 출력
pd.set_option("display.max_columns", None)    # 컬럼 생략 없이 모두 출력
pd.set_option("display.max_colwidth", None)   # 셀 내용 길이 제한 없애기
pd.set_option("display.expand_frame_repr", False)  # 출력 시 줄바꿈 방지

def preprocess(text: str) -> str:
    # NaN, None 방지
    if text is None or (isinstance(text, float) and np.isnan(text)):
        return ""
    # 혹시 리스트/숫자 등이 들어와도 문자열로 강제 변환
    text = str(text)
    # HTML 태그 제거 (있다면)
    text = re.sub(r"<.*?>", "", text)
    # 개행/탭 -> 공백
    text = text.replace("\n", " ").replace("\r", " ").replace("\t", " ")
    # 공백 여러 개 -> 하나로
    text = re.sub(r"\s+", " ", text).strip()
    return text

with open(r"D:\STUDY\project\get_data\data\model\model1.pkl", "rb") as f:
    model1 = joblib.load(f)

df = pd.read_csv(file_path, encoding="utf-8-sig")
new_df = df[df["art_cat"].isin(["정치","경제","국제(세계)","사회","생활/문화","스포츠"])].dropna()
x = new_df['art_title']+" "+new_df['art_desc'].apply(preprocess)
y = new_df['art_cat']

print(model1.score(x,y))

