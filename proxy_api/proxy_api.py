
import json
import re
import time
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
APIKEY = ""

OPENAI_CHAT_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODELS_URL = "https://api.openai.com/v1/models"
HEADERS = {"Authorization":"Bearer " + APIKEY, "Content-Type": "application/json" }
# add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def request_chat(data: dict):
    resp = requests.post(OPENAI_CHAT_URL, headers=HEADERS, data=json.dumps(data))
    if resp.status_code != 200:
        return {"message":"status not 200 from openai"}
    return resp.json()


def request_models():
    resp = requests.get(OPENAI_MODELS_URL, headers=HEADERS)
    if resp.status_code != 200:
        return {"message":"status not 200 from openai"}
    return resp.json()


@app.post("/v1/chat/completions")
async def post_data(data: dict):
    print("POST /v1/chat/completions")
    return request_chat(data)


@app.get('/v1/models')
async def list_models():
    print("GET /v1/models")
    """Returns a list of models to get app to work."""

    return request_models()


@app.post('/')
async def post_data(data: dict):
    """Basic route for testing the API works"""
    result = {"message": "Data received", "data": data}
    return result
