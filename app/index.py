from flask import Flask
app = Flask(__name__)

@app.get("/")
def app_index():
    return {"message": "Hello from app/index.py!"}
