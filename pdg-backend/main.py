from fastapi import FastAPI
from models import PatientDataModel
from services import model_prediction

app = FastAPI()

base_url = "/api/v1"

@app.get(base_url+"/")
def read_root():
    return {"Hello": "World"}
  
@app.post(base_url+"/rf_model")
def predict_rf_model(input_data: PatientDataModel.PatientInput):
  #return input_data
  return model_prediction.predict_random_forest_model(input_data)
  
@app.post(base_url+"/xgb_model")
def predict_xgb_model(input_data: PatientDataModel.PatientInput):
    return model_prediction.predict_xgboost_model(input_data)
  
print("Server started at http://")


