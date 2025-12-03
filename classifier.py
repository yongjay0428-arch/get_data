import pandas as pd
import json
import sklearn.feature_extraction.text as text
import joblib

from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
file_path = r"/data/전처리/news_train_dataset.json1"
test_file_path = r""

with open(file_path, "r", encoding="utf-8-sig") as f:
    dataset = pd.read_json(f, lines=True, encoding="utf-8-sig")

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
joblib.dump(model1, "data/model/model1.pkl")






