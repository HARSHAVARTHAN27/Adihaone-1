from flask import Flask
app = Flask(__name__)

@app.get("/")
def app_app():
    return {"message": "Hello from app/app.py!"}
