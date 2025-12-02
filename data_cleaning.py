import pandas as pd
import os
import json

from collections import Counter

save_dir ="keywords"
file_name = "meta_work_19981231.csv"

file_path = os.path.join("data", file_name)
os.makedirs(save_dir, exist_ok=True)

save_path = os.path.join(save_dir, 'keywords.json')
df = pd.read_csv(f"{file_path}",encoding="cp949")
result = df["키워드"].str.split(',').sum()
counter = Counter(result)

with open(save_path, mode='w', encoding='utf-8') as f:
    json.dump(counter, f, ensure_ascii=False, indent=2)
