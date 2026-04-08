# 🎵 SoundSense — Audio Instrument Classifier GUI

A Flask web app with a beautiful GUI for your ML-based musical instrument classifier.

## Project Structure

```
audio_classifier/
├── app.py                    ← Flask backend
├── instrument_model.pkl      ← Your trained model (ADD THIS)
├── label_encoder.pkl         ← Your label encoder (ADD THIS)
├── uploads/                  ← Temp upload dir (auto-created)
└── templates/
    └── index.html            ← Frontend GUI
```

## Setup Instructions

### 1. Add Your Model Files
Copy your trained model files into this directory:
```
instrument_model.pkl
label_encoder.pkl
```
These should already exist in your Google Drive at:
`/content/drive/MyDrive/archive/music_dataset/music_dataset/`

### 2. Install Dependencies
```bash
pip install flask librosa numpy scikit-learn joblib
```

### 3. Run the App
```bash
python app.py
```
Open your browser at: **http://localhost:5000**

---

## Running in Google Colab (with ngrok)
```python
from pyngrok import ngrok
import threading

ngrok.set_auth_token("YOUR_TOKEN")
public_url = ngrok.connect(5000)
print(f"App is live at: {public_url}")

# Run Flask in a thread
threading.Thread(target=lambda: app.run(port=5000)).start()
```

---

## Features
- 🎼 Drag & drop audio upload (WAV, MP3, OGG, FLAC, M4A)
- 📊 Live waveform visualization
- 🎯 Top-5 prediction probabilities with animated bars
- 🎸 Identifies 30+ instruments (Piano, Violin, Guitar, Saxophone, etc.)
- ⚡ MFCC feature extraction via librosa

## How It Works
1. User uploads an audio file
2. Flask extracts 40 MFCC features over 130 frames (same as training)
3. The sklearn model predicts the instrument class
4. Top-5 predictions + confidence scores are returned to the UI
