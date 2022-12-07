from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn
import numpy as np

from Apartment import Apartment

app = FastAPI()

preprocess = pickle.load(open('../models/prep_pipe.pkl','rb'))
model = pickle.load(open('../models/model.pkl','rb'))

# class PredictionOut(BaseModel):
#     Price:int



@app.get("/")
def home():
    return "Welcome to TAP: The Apartment People"


@app.post("/predict")
def predict_price(data:Apartment):
    data = dict(data)
    # print(data)
    
    year_built = data['year_built']
    floor = data['floor']
    size_sqf = data['size_sqf']
    hallway = data['hallway']
    heating = data['heating']
    management = data['management']
    nearest_subway = data['nearest_subway']
    time_to_subway = data['time_to_subway']
    time_to_bus_stop = data['time_to_bus_stop']
    # facilities = data['facilities']
    parking_basement = data['parking_basement']

    cols = ['YearBuilt','Floor','HallwayType','HeatingType','AptManageType',
            'TimeToBusStop','TimeToSubway','SubwayStation',
            'Size(sqf)','N_Parkinglot(Basement)']

    values = [year_built,floor,hallway,heating,management,
            time_to_bus_stop,time_to_subway,nearest_subway,
            size_sqf,parking_basement]

    
    prepped_features = preprocess.transform(pd.DataFrame(np.array(values).reshape(1,10),columns=cols))

    pred_price = model.predict(prepped_features)

    return round(pred_price[0],2)

if __name__ == '__main__':
    uvicorn.run(app, port=8000)