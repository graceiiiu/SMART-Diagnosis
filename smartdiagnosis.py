 import streamlit as st
from fastapi import FastAPI, Request
import tensorflow as tf

app = FastAPI()

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    
    # Process the audio file
    audio_file = data['audio_file']
    
    # Make prediction using your model
    prediction = your_model.predict(processed_audio)
    
    return {"prediction": str(prediction)}
