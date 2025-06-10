# Spam Detection Project

This project implements a spam detection system using machine learning. It includes both a web application and an Android app for detecting spam messages.

## Features

- Machine learning-based spam detection
- Web interface for message checking
- Android app for mobile access
- High accuracy spam classification

## Project Structure

- `app.py`: Flask web application
- `email-spam-detection-98-accuracy.ipynb`: Jupyter notebook containing model training
- `spam.csv`: Dataset for training
- `text_clf_svm_model.joblib`: Trained model file
- `templates/`: Web interface templates

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/Aakashjayshri07/spam-detection.git
cd spam-detection
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Run the web application:
```bash
python app.py
```

## Usage

1. Web Application:
   - Open your browser and navigate to `http://localhost:5000`
   - Enter a message in the text field
   - Click "Check Spam" to get the prediction

2. Android App:
   - Build and install the Android app from the `app` directory
   - Make sure the web server is running
   - Enter a message and tap "Check for Spam"

## Model Details

The spam detection model is trained using:
- CountVectorizer for text feature extraction
- Multinomial Naive Bayes classifier
- Achieves high accuracy in spam detection

## License

This project is licensed under the MIT License - see the LICENSE file for details. 