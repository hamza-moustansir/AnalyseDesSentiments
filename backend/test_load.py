import pickle

try:
    with open('app/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('app/tfidf.pkl', 'rb') as tfidf_file:
        tfidf = pickle.load(tfidf_file)

    print("Chargement réussi :")
    print(f"Modèle : {type(model)}")
    print(f"TF-IDF : {type(tfidf)}")

except Exception as e:
    print(f"Erreur lors du chargement : {e}")
