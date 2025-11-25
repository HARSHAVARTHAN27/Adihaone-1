from flask import Flask

app = Flask(__name__)

@app.get("/")
def read_root():
    return {"Python": "on Vercel"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)

