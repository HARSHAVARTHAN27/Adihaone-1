from flask import Flask
app = Flask(__name__)

@app.get("/")
def src_app():
    return {"message": "Hello from src/app.py!"}
