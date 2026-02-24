from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "demo-service", "ok": True}

@app.get("/health")
def health():
    return {"status": "healthy"}