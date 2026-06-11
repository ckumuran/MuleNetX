from fastapi import FastAPI

app = FastAPI(
    title="MuleNetX API",
    description="Graph-Based Financial Crime Intelligence Platform",
    version="2.0.0"
)

@app.get("/")
def root():
    return {
        "platform": "MuleNetX",
        "status": "online",
        "version": "2.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/system")
def system():
    return {
        "backend": "online",
        "neo4j": "pending",
        "postgres": "pending",
        "ml_engine": "pending",
        "copilot": "pending"
    }
