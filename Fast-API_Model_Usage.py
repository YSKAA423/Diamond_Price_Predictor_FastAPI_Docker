# for data validation (usually imported but will make it here for ease of use)
# Used in order to make sure that users enter the right inputs for the models

from pydantic import BaseModel
import os

class DiamondPricePredictor(BaseModel):
    carat:float
    cut:int
    color:int
    clarity:int
    x_over_y:float
    z_over_y:float
    depth:float
    table:float

import joblib
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "diamond_price_predictor.joblib")
model = joblib.load(model_path)

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def index():
    return """
        <html>
            <body>
                <h2>Diamond Price Predictor Machine Learning API</h2>
                <p>This API provides an endpoint for predicting diamond prices based on various attributes.</p>

                <h3>Available Endpoints:</h3>
                <ul>
                    <li><code>/docs</code>: Go to this URL to access the documentation page (provided by FastAPI), where you can test the model (via the "Try it out" button in POST) and get predictions.</li>
                </ul>

                <h3>Model Parameters:</h3>
                <ul>
                    <li><code>carat</code> (float): Weight of the diamond in carats.</li>
                    <li><code>cut</code> (int): Quality of the cut, from 1 (Fair) to 5 (Ideal).</li>
                    <li><code>color</code> (int): Color rating of the diamond, from 1 (J, worst) to 7 (D, best).</li>
                    <li><code>clarity</code> (int): Clarity rating, from 1 (I1, worst) to 8 (IF, best).</li>
                    <li><code>x_over_y</code> (float): Ratio of the diamond's length over width.</li>
                    <li><code>z_over_y</code> (float): Ratio of the diamond's depth over width.</li>
                    <li><code>depth</code> (float): Total depth percentage, calculated as <code>z / mean(x, y)</code> or <code>2 * z / (x + y)</code>.</li>
                    <li><code>table</code> (float): Width of the diamond's top relative to its widest point.</li>
                </ul>

                <p><strong>Note:</strong> This model provides estimates for fun and educational purposes only. So if you're looking for a diamond to impress, maybe don’t take these prices to your local jeweler just yet! 💎</p>
                <a href="/docs"><button type="button">Click Me to go docs</button></a>
            </body>
        </html>
    """





@app.post('/diamond/predict')
def predict_diamond_price(data:DiamondPricePredictor):
    data = data.model_dump() 

    inputs = list(data.values())
    
    prediction = model.predict([inputs])

    return {'prediction': prediction[0]}


if __name__ == '__main__':
    # For local testing only. Not needed if deploying on a server.
    uvicorn.run(app, host='0.0.0.0', port=8000)
