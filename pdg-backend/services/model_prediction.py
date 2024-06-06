import joblib
import pandas as pd
import os

def predict_random_forest_model(input_data: dict) -> dict:
  
    data_df = pd.DataFrame(input_data)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..\\mlModels\\rf_model.pkl')
    
    print(f"Model path: {model_path}")
    # Load the model
    model = joblib.load(model_path)

    # Make prediction
    prediction = model.predict(data_df)

    return prediction


def predict_xgboost_model(input_data: dict) -> dict:
  
    data_df = pd.DataFrame(input_data)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..\\mlModels\\xgb_clf_model.pkl')
  
    # Load the model
    model = joblib.load(model_path)

    # Make prediction
    prediction = model.predict(data_df)

    return prediction


