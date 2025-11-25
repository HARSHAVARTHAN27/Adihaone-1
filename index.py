from flask import Flask
app = Flask(__name__)

@app.get("/")
def index_root():
    return {"message": "Hello from root index.py!"}
