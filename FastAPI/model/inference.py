import pandas as pd 
from pycaret.regression import load_model, predict_model


model = load_model('model/diamond-pipeline')

def inference(input: pd.DataFrame) -> dict():
    predictions = predict_model(model, data = input)

    return {'prediction' : int(predictions['Label'][0])}
    
