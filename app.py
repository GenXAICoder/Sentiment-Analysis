from flask import Flask, request
import pickle

app = Flask(__name__)

@app.get("/")
def index():
    return "hello world"

@app.post("/predict")
def predict():
    try:
        data = request.json
        
        review = data.get("review", None)
        print(review)
        if not review:
            return {"error": "review is required"}, 400

        #   Load the model from the pickle file
        model = pickle.load(open("model_LGBMClassifier.pkl", "rb"))
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
        
        review = vectorizer.transform([review])
        
        prediction = model.predict(review)
        if len(prediction) == 0:
            return {"error": "Couldn't predict"}, 400
        
        output_map = {
            0: "Neutral Review",
            1: "Negative Review",
            2: "Positive Review"
        }

        return {
            "prediction": output_map[prediction[0].item()]
        }, 200
        
    except Exception as e:
        print(e)

