import pickle

def load_model():
    try:
        with open('model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        with open('tfidf.pkl', 'rb') as tfidf_file:
            tfidf = pickle.load(tfidf_file)
        return model, tfidf
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None, None
