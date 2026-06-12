from fastapi import FastAPI

app = FastAPI(
    title="MuleNetX"
)


@app.get("/")
def health():

    return {
        "status": "running",
        "service": "MuleNetX"
    }
