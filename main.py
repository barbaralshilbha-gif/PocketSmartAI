from fastapi import FastAPI

app = FastAPI(title="PocketSmart AI")


@app.get("/")
def home():
    return {
        "message": "PocketSmart AI is running successfully!"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }