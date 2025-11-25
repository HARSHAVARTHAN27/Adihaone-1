from flask import Flask
app = Flask(__name__)

@app.get("/")
def server_root():
    return {"message": "Hello from root server.py!"}
