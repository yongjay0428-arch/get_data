import pandas as pd
import json
import sklearn.feature_extraction.text as text
import joblib

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from class_test import preprocess

file_path = r"D:\STUDY\project\get_data\data\전처리\news_train_dataset.json1"

dataset = pd.read_json(file_path, lines=True, encoding="utf-8-sig")
dataset.dropna(inplace=True)

dataset["title"] = dataset["title"].apply(preprocess)
dataset["content"] = dataset["content"].apply(preprocess)

x =  dataset["title"]+" "+dataset["content"]
y = dataset["category"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

model1 = Pipeline([
  ('vect',text.TfidfVectorizer(
      analyzer='char',
      ngram_range=(3,5),
      min_df=3
  )),
  ('model', LinearSVC(
      class_weight="balanced",
      C=1.5,
      max_iter=3000,
  ))
])

model1.fit(x_train,y_train)
score = model1.score(x_test,y_test)
print(f"model1:{score}점")
print("저장시작")
joblib.dump(model1, "data/model/model_v2.pkl")






