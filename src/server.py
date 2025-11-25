from flask import Flask
app = Flask(__name__)

@app.get("/")
def src_server():
    return {"message": "Hello from src/server.py!"}
