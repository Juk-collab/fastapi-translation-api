import requests

# Define the URL of your FastAPI server
url = "http://127.0.0.1:8000/secure-translate/"

# Parameters for the translation
params = {
    "text": "Hello, how are you?",
    "target_language": "fi"
}

# Define the headers with the API key
headers = {
    "X-API-KEY": "your_api_token_here"
}

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Check if the response is successful (status code 200)
if response.status_code == 200:
    translation = response.json()
    print(f"Original Text: {translation['original_text']}")
    print(f"Translated Text: {translation['translated_text']}")
else:
    print("Error:", response.status_code)