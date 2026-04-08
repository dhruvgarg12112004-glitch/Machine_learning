import os
import numpy as np
import librosa
import joblib
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac', 'm4a'}

# Load model and label encoder
MODEL_PATH = 'instrument_model.pkl'
ENCODER_PATH = 'label_encoder.pkl'

model = None
label_encoder = None

def load_models():
    global model, label_encoder
    try:
        model = joblib.load(MODEL_PATH)
        label_encoder = joblib.load(ENCODER_PATH)
        print("✅ Model and label encoder loaded successfully.")
    except Exception as e:
        print(f"⚠️  Could not load model: {e}")
        print("    Place 'instrument_model.pkl' and 'label_encoder.pkl' in the same directory.")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_features(file_path):
    """Extract 40 MFCC features, padded/truncated to 130 frames."""
    max_pad_len = 130
    audio, sr = librosa.load(file_path, duration=3)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    pad_width = max_pad_len - mfcc.shape[1]
    if pad_width > 0:
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :max_pad_len]
    return mfcc

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': f'Unsupported file type. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'}), 400

    if model is None or label_encoder is None:
        return jsonify({'error': 'Model not loaded. Place instrument_model.pkl and label_encoder.pkl in the app directory.'}), 500

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    try:
        mfcc = extract_features(file_path)
        features = mfcc.flatten().reshape(1, -1)

        # Get prediction and probabilities
        prediction = model.predict(features)[0]
        predicted_label = label_encoder.inverse_transform([prediction])[0]

        # Get top-5 probabilities if available
        top_predictions = []
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(features)[0]
            top_indices = np.argsort(probabilities)[::-1][:5]
            top_predictions = [
                {
                    'label': label_encoder.inverse_transform([i])[0].replace('_', ' '),
                    'confidence': round(float(probabilities[i]) * 100, 1)
                }
                for i in top_indices
            ]

        os.remove(file_path)
        return jsonify({
            'prediction': predicted_label.replace('_', ' '),
            'top_predictions': top_predictions
        })

    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

if __name__ == '__main__':
    load_models()
    app.run(debug=True, port=5000)
