import pickle
from flask import request, jsonify
from .utils import clean_text

# Charger le modèle
try:
    with open('app/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('app/tfidf.pkl', 'rb') as tfidf_file:
        tfidf = pickle.load(tfidf_file)

except Exception as e:
    print(f"Erreur lors du chargement des fichiers : {e}")
    model = None
    tfidf = None

def predict_sentiment():
    try:
        if model is None or tfidf is None:
            raise ValueError("Le modèle ou le TF-IDF n'a pas été chargé correctement.")

        data = request.get_json()
        text = data.get('text', '')

        # Nettoyer le texte
        cleaned_text = clean_text(text)

        # Vectoriser le texte
        text_vector = tfidf.transform([cleaned_text])

        # Prédire le sentiment
        prediction = model.predict(text_vector)[0]
        sentiment = 'positive' if prediction == 1 else 'negative'

        # Retourner le résultat
        return jsonify({'sentiment': sentiment})

    except Exception as e:
        return jsonify({'error': str(e)})
