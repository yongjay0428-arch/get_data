import pandas as pd
import os 
import json
import bs4
from bs4 import BeautifulSoup

file_path = r"D:\STUDY\project\get_data\data"
file_list = os.listdir(file_path)
save_file = "data/전처리/news_train_dataset.json1"

seen = set()

with open(save_file,"w",encoding="utf-8") as out_f:
    for file in file_list:
        # print(file)
        with open(f'data/{file}', 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            # print(json.dumps(data, indent=2, ensure_ascii=False))
        for item in data["data"]:
            record = {
                "category": item["doc_class"]["code"],
                "title": item["doc_title"],
                "content": item["paragraphs"][0]["context"].replace("\n", "")
            }

            # 제목 기준 중복 제거
            key = record["title"]  # 굳이 json.dumps 안 써도 됨
            if key in seen:
                continue
            seen.add(key)

            # jsonl 한 줄 쓰기
            out_f.write(json.dumps(record, ensure_ascii=False) + "\n")