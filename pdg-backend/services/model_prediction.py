import joblib
import pandas as pd
import os

def predict_random_forest_model(input_data: dict) -> any:
  
    data_df = pd.DataFrame([input_data], index=[0])
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '../mlModels/rf_model.pkl')
    
    # Load the model
    model = joblib.load(model_path)

    # Make prediction
    prediction = model.predict(data_df)

    return prediction.tolist()


def predict_xgboost_model(input_data: dict) -> any:
  
    data_df = pd.DataFrame([input_data], index=[0])
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '../mlModels/xgboost_model.pkl')
  
    # Load the model
    model = joblib.load(model_path)

    # Make prediction
    prediction = model.predict(data_df)

    return prediction.tolist()


