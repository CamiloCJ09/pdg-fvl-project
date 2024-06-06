import joblib
import pandas as pd

def predict_random_forest_model(input_data: dict) -> dict:
  
    data_df = pd.DataFrame(input_data)
    # Load the model
    model = joblib.load('pdg-backend\\mlModels\\xgb_clf_model.pkl')

    # Make prediction
    prediction = model.predict(data_df)

    return prediction


def predict_xgboost_model(input_data: dict) -> dict:
  
    data_df = pd.DataFrame(input_data, index=[1])
  
    # Load the model
    model = joblib.load('pdg-backend/aiModels/xgb_clf_model.pkl')

    # Make prediction
    prediction = model.predict(data_df)

    return prediction


