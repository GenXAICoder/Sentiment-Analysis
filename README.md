# Sentiment-Analysis
This project provides a RESTful API to perform sentiment analysis on text reviews. It uses a Flask-based backend with a pre-trained machine learning model.


## Prerequisites

Ensure you have the following installed:

- Python 3.8 or above
- `pip` package manager

## Installation and Setup

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. Ensure the model and vectorizer files are present:
   - model_LGBMClassifier.pkl: Pre-trained classification model.
   - vectorizer.pkl: Pre-trained text vectorizer. Place these files in the root directory of the project.

## Running the Application
1. Start the Flask server:
   ```bash
   python app.py
2. API Endpoints:
   - GET /: Returns a "hello world" message to verify the server is running.
   - POST /predict: Request Body (JSON)
     ```bash
     {
      "review": "Your review text here"
     }
    - Response
      ```bash
      {
      "prediction": "Positive Review"
      }
