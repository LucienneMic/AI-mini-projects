from fastapi import FastAPI
import requests

app = FastAPI()

AI_SERVICE_URL = "http://ai-service:8001"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/prompt")
def send_prompt(prompt: str):
    response = requests.post(
        f"{AI_SERVICE_URL}/generate",
        json={"prompt": prompt}
    )
    return response.json()
