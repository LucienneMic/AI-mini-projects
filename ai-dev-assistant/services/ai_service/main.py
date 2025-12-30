from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(prompt: dict):
    return {
        "response": f"AI response for: {prompt['prompt']}"
    }
