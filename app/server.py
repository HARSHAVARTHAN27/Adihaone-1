from flask import Flask
app = Flask(__name__)

@app.get("/")
def app_server():
    return {"message": "Hello from app/server.py!"}
