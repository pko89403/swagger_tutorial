import pandas as pd 
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 



from model.inference import inference
from app.models import HistoryItem, PredictItem
import app.history as history


# Create the app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://localhost:3000', 'localhost:3000'],
    allow_credentials = True, 
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/history")
async def get_histories():
    response = await history.fetch_all_histories()
    return response

@app.post("/history")
async def post_history(historyItem: HistoryItem):
    response = await history.update_history(historyItem)
    return response

# Define predict function 
@app.post('/predict')
def predict(predictItem: PredictItem):
    
    data = pd.DataFrame([[int(predictItem.carat_weight),
                        predictItem.cut,
                        predictItem.color,
                        predictItem.clarity,
                        predictItem.polish,
                        predictItem.symmetry,
                        predictItem.report]])

    data.columns = ['Carat Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report']

    prediction = inference(data)

    return prediction


@app.get('/')
def home():
    return {'name' : 'pycaret fastAPI'}

def get_app():
    return app

            