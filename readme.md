This is a simple API made with FastAPI, translates text to desired language

requirements by running this:
pip install fastapi uvicorn googletrans==4.0.0-rc1, requests


API can be launched from the project folder with
uvicorn app:app --reload

Then see test.py how it can be used.
Running test.py currently translates example sentence from english to finnish.
