from flask import Flask, request, jsonify
from flask_cors import CORS  
from app.routes import predict_sentiment

app = Flask(__name__)

CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    from app.routes import predict_sentiment
    return predict_sentiment()

@app.route('/', methods=['GET'])
def home():
    return "L'API de classification des sentiments fonctionne !"

if __name__ == '__main__':
    app.run(debug=True)
