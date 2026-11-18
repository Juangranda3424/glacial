from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "microservice-commercial"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host="127.0.0.1", port=config.port, reload=True)