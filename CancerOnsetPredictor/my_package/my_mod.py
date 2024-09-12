import os
from joblib import load

def load_high_model():
    model_path = os.path.join(os.path.dirname(__file__), 'rf_final_high_model.joblib')
    return load(model_path)

def load_low_model():
    model_path = os.path.join(os.path.dirname(__file__), 'rf_final_low_model.joblib')
    return load(model_path)

def predict_high(input_data):
    model = load_high_model()
    return model.predict(input_data)

def predict_low(input_data):
    model = load_low_model()
    return model.predict(input_data)