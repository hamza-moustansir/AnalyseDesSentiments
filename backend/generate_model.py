import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import re

# Charger les données
data = pd.read_csv('IMDB Dataset.csv')

# Nettoyer les textes
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

data['cleaned_review'] = data['review'].apply(clean_text)

# Vectorisation TF-IDF
tfidf = TfidfVectorizer(max_features=500)
X = tfidf.fit_transform(data['cleaned_review']).toarray()
y = data['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

# Division des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Sauvegarder les fichiers
with open('app/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('app/tfidf.pkl', 'wb') as tfidf_file:
    pickle.dump(tfidf, tfidf_file)

print("Modèle et TF-IDF enregistrés avec succès.")
