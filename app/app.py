from flask import Flask
app = Flask(__name__)

@app.get("/")
def root():
    return "Hello from CI/CD build!\n", 200

@app.get("/healthz")
def health():
    return "ok\n", 200
