import pandas as pd
data2 = pd.read_csv('jobs.csv')

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import joblib

data2["Description"] = data2["Description"].str.lower() 
data2["Description"] = data2["Description"].str.replace("[^a-zA-Z0-9 ]", "", regex=True)  

vectorizer_0 = TfidfVectorizer(max_features=1000)
features = vectorizer_0.fit_transform(data2["Description"])

X_train, X_test, y_train, y_test = train_test_split(features, data2["Skill Set"], test_size=0.2)

model_0 = RandomForestClassifier()
model_0.fit(X_train, y_train)

y_pred = model_0.predict(X_test)

f1 = f1_score(y_test, y_pred, average="micro")
print('Model for skills extraction from job descriptions loaded...')
print(f"F1-score (micro): {f1:.4f}")

# joblib.dump(model2,'job_.pkl')

def prediction(description):

    new_features = vectorizer_0.transform(description)
    predictions = model_0.predict(new_features)
    return predictions