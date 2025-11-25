from flask import Flask
app = Flask(__name__)

@app.get("/")
def src_index():
    return {"message": "Hello from src/index.py!"}
