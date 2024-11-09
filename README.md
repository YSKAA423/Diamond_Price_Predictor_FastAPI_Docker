# Diamond Price Predictor API

This is a FastAPI application that uses a machine learning model to predict the price of a diamond based on various attributes. The model itself can be found in the original project repository [Diamond Price Predictor](https://github.com/YSKAA423/Diamond_Price_Predictor).

## Project Setup

Note: The model (.joblib) has been compressed in order to push it to GitHub decompress the model and make sure it exists in the same directory as the code and dockerfile.

### 1. Docker Setup

To run this project using Docker:

- Pull the Docker image (optional, if you want to start from a pre-built image):
  ```bash
  docker pull yskaa/diamond_price_predictor
  ```

  OR

- Build the Docker image from the Dockerfile:
  ```bash
  docker build -t diamond_price_predictor .
  ```

  ```bash
  docker build -t diamond_price_predictor /path/to/folder  # Replace with the actual folder path
  ```

- Run the Docker container:
  ```bash
  docker run -p 8000:8000 diamond_price_predictor
  ```
  
  # -d detaches the container to use the terminal afterwards and -p is done for port binding

- Access the API at `http://localhost:8000`.

### 2. Local Setup (Without Docker)

If you want to run the application locally (without Docker):

- Install the required dependencies:
  ```bash
  pip install pydantic joblib fastapi uvicorn scikit-learn
  ```

- Run the FastAPI application:
  ```bash
  uvicorn Fast-API_Model_Usage.py:app --host 0.0.0.0 --port 8000
  ```
  Or simply run the code in any IDE of choice. 

- Access the API at `http://localhost:8000`.

## Available Endpoints

- `/`: Welcome page explaining the API.
- `/docs`: Access FastAPI's auto-generated documentation and try out the model via the interactive "Try it out" button.
- `/diamond/predict`: Predict diamond price by providing the following parameters in a POST request.

### Model Parameters:

- **carat** (float): Weight of the diamond in carats.
- **cut** (int): Quality of the cut (1 to 5).
- **color** (int): Color rating (1 to 7).
- **clarity** (int): Clarity rating (1 to 8).
- **x_over_y** (float): Ratio of length over width.
- **z_over_y** (float): Ratio of depth over width.
- **depth** (float): Total depth percentage.
- **table** (float): Width of the diamond's top.

## Example of Predicting Diamond Price

Make a POST request to `/diamond/predict` with the following JSON body:

```json
{
    "carat": 0.5,
    "cut": 5,
    "color": 6,
    "clarity": 6,
    "x_over_y": 1.2,
    "z_over_y": 0.8,
    "depth": 61.2,
    "table": 57.0
}
```

Response:

```json
{
    "prediction": 3500.12
}
```

## Note

This is a fun and educational project. The predictions should not be taken seriously for actual diamond pricing. For the model and its details, please refer to the [original project repository](https://github.com/YSKAA423/Diamon_Price_Predictor).

