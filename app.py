from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import os
from flask_cors import CORS
# Load the trained model
model_file = 'text_clf_svm_model.joblib'
text_clf = joblib.load(model_file)

# Create a Flask application
app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text from the request
        data = request.json
        text = data.get('text', '')

        # Predict using the loaded model
        prediction = text_clf.predict([text])

        # Create a response
        if prediction[0] == 1:
            result = 'spam'
        else:
            result = 'Not spam'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




