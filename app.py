import requests
from fastapi import FastAPI
from pydantic import BaseModel

from utils.AppConfig import AppConfig

config = AppConfig()
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/opt-1.3b"
HF_API_KEY = config.get_hf_api_key()

class PromptRequest(BaseModel):
    prompt: str

app = FastAPI()


@app.post("/generate")
async def generate_text(request: PromptRequest):
    prompt = request.prompt
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(HF_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return {"response": response.json()}
    else:
        return {"error": response.text}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
