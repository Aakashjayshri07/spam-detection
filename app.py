<<<<<<< HEAD
# from flask import Flask, request, jsonify, render_template
# import joblib  # or import pickle if you prefer
# import pandas as pd

# # Load the trained model
# model_file = 'text_clf_svm_model.joblib'  # Change to .pkl if using pickle
# text_clf = joblib.load(model_file)

# # Create a Flask application
# app = Flask(__name__)

# # Home route
# @app.route('/')
# def home():
#     return render_template('index.html')  # Create an HTML file for the interface

# # Route for prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the text from the request
#     data = request.json  # Expecting JSON input
#     text = data.get('text', '')  # Get the text, default to empty string

#     # Predict using the loaded model
#     prediction = text_clf.predict([text])

#     # Create a response
#     # result = 'spam' if prediction[0] == 1 else 'ham'  # Assuming 1 is spam and 0 is ham

#     # return jsonify({'prediction': result})

#     if prediction[0] == 1:
#         st.success("This message is **Spam**!")
#     else:
#             st.success("This message is **Ham**!")
 

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, request, jsonify, render_template
import joblib  # or import pickle if you prefer
import pandas as pd

# Load the trained model
model_file = 'text_clf_svm_model.joblib'  # Change to .pkl if using pickle
text_clf = joblib.load(model_file)

# Create a Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Create an HTML file for the interface

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the text from the request
    data = request.json  # Expecting JSON input
    text = data.get('text', '')  # Get the text, default to empty string

    # Predict using the loaded model
    prediction = text_clf.predict([text])

    # Create a response
    if prediction[0] == 1:
        result = 'spam'
        print("result") 
    else :
        result="Not spam"  # Assuming 1 is spam and 0 is ham
    return jsonify({'prediction': result})
    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)




=======
# from flask import Flask, request, jsonify, render_template
# import joblib  # or import pickle if you prefer
# import pandas as pd

# # Load the trained model
# model_file = 'text_clf_svm_model.joblib'  # Change to .pkl if using pickle
# text_clf = joblib.load(model_file)

# # Create a Flask application
# app = Flask(__name__)

# # Home route
# @app.route('/')
# def home():
#     return render_template('index.html')  # Create an HTML file for the interface

# # Route for prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the text from the request
#     data = request.json  # Expecting JSON input
#     text = data.get('text', '')  # Get the text, default to empty string

#     # Predict using the loaded model
#     prediction = text_clf.predict([text])

#     # Create a response
#     # result = 'spam' if prediction[0] == 1 else 'ham'  # Assuming 1 is spam and 0 is ham

#     # return jsonify({'prediction': result})

#     if prediction[0] == 1:
#         st.success("This message is **Spam**!")
#     else:
#             st.success("This message is **Ham**!")
 

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, request, jsonify, render_template
import joblib  # or import pickle if you prefer
import pandas as pd

# Load the trained model
model_file = 'text_clf_svm_model.joblib'  # Change to .pkl if using pickle
text_clf = joblib.load(model_file)

# Create a Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Create an HTML file for the interface

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the text from the request
    data = request.json  # Expecting JSON input
    text = data.get('text', '')  # Get the text, default to empty string

    # Predict using the loaded model
    prediction = text_clf.predict([text])

    # Create a response
    if prediction[0] == 1:
        result = 'spam'
        print("result") 
    else :
        result="Not spam"  # Assuming 1 is spam and 0 is ham
    return jsonify({'prediction': result})
    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)




>>>>>>> 54a46582245d7c120b67f0d61c36592f5dcb64f4
