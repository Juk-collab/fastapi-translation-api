from fastapi import FastAPI
from googletrans import Translator

app = FastAPI()

# Create a route for translating text
@app.get("/translate/")
async def translate_text(text: str, target_language: str):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return {"original_text": text, "translated_text": translation.text}

# If you want to access a health check
@app.get("/")
def read_root():
    return {"message": "FastAPI Translation API is running!"}


from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY = "your_api_token_here"  # This would of course be changed if deployed
api_key_header = APIKeyHeader(name="X-API-KEY")

# Dependency to verify the API key
def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return api_key

@app.get("/secure-translate/")
async def secure_translate(text: str, target_language: str, api_key: str = Depends(get_api_key)):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return {"original_text": text, "translated_text": translation.text}