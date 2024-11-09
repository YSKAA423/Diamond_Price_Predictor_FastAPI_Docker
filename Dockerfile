FROM python:3.12.5-slim

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir pydantic joblib fastapi uvicorn scikit-learn

EXPOSE 8000

CMD [ "uvicorn", "Fast-API_Model_Usage:app","--host","0.0.0.0","--port","8000" ]

# Step 1: Use a slim Python 3.12 image as the base image
# Step 2: Copy the contents of your current directory into the /app directory inside the container
# Step 3: Set the /app directory as the working directory inside the container
# Step 4: Install the necessary Python dependencies without using the cache
# (Expose shows the port that Fast-API will run on but a port binding is needed when running the container)
# Step 6: Define the default command to run your FastAPI app using Uvicorn when the container starts