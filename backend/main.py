from fastapi import FastAPI

from backend.routes.investigation import router

app = FastAPI(
    title="MuleNetX"
)

app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def health():

    return {
        "status": "running"
    }
