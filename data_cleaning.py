from collections import Counter
import pandas as pd
import os, json

save_dir = "keywords"
file_name = "meta_work_19981231.csv"

file_path = os.path.join("data", file_name)
os.makedirs(save_dir, exist_ok=True)

save_path = os.path.join(save_dir, 'keywords.json')

# ① 필요한 컬럼만 읽기
df = pd.read_csv(file_path, encoding="cp949", usecols=["키워드"])

counter = Counter()

# ② 중간 리스트 없이 바로 Counter 업데이트
for text in df["키워드"].dropna():
    counter.update(text.split(','))

# ③ 저장
with open(save_path, mode='w', encoding='utf-8') as f:
    json.dump(counter, f, ensure_ascii=False, indent=2)

