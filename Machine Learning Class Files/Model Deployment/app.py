import pickle
import numpy as np
from flask import Flask, request, jsonify
# from flask_cors import CORS  # <-- Import CORS
import flask_cors

app = Flask(__name__)
# CORS(app)  # <-- Enable CORS for all routes
flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})  # <-- Allow all origins

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained machine learning model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Parse JSON data from the incoming request
        data = request.get_json()
        
        # 2. Extract features (expects a list of features, e.g., [5.1, 3.5, 1.4, 0.2])
        features = np.array(data['features']).reshape(1, -1)
        
        # 3. Generate prediction
        prediction = model.predict(features)
        
        # 4. Return the prediction result as JSON
        return jsonify({
            'status': 'success',
            'prediction': int(prediction[0])
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    # Run the local development server
    app.run(debug=True, port=5000)
