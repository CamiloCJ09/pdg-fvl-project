from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import PatientDataModel
from services import model_prediction

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base_url = "/api/v1"

@app.get(base_url+"/")
def read_root():
    return {"Hello": "World"}
  
@app.post(base_url+"/rf_model")
def predict_rf_model(input_data: PatientDataModel.PatientInput):
  input_dict = input_data.dict(by_alias=True)
  #return input_data
  return model_prediction.predict_random_forest_model(input_dict)
  
@app.post(base_url+"/xgb_model")
def predict_xgb_model(input_data: PatientDataModel.PatientInput):
    input_dict = input_data.dict(by_alias=True)
    return model_prediction.predict_xgboost_model(input_dict)
  


