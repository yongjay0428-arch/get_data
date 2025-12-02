import pandas as pd
import os 
import json

file_path = "D:\STUDY\project\get_data\data"
file_list = os.listdir(file_path)
save_file = "news_train_dataset.json1"

result = []
dedupe_result =[]
seen = set()

with open(save_file,"w",encoding="utf-8") as out_f:
    for file in file_list:
        # print(file)
        with open(f'data/{file}', 'r', encoding="utf-8") as f:
            data = json.load(f)
            # print(json.dumps(data, indent=2, ensure_ascii=False))
        for item in data["data"]:
            result.append( [
                {
                    "category":item["doc_class"]["code"],
                    "title":item["doc_title"],
                    "content":item["paragraphs"][0]["context"]
                }
            ] )
    
    for item in result:
        key = json.dumps(item[0]["title"], ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            dedupe_result.append(item)

    out_f.write(json.dumps(dedupe_result,ensure_ascii=False,indent=2))
    # out_f.write(json.dumps(result,ensure_ascii=False,indent=2))