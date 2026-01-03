from fastapi import FastAPI
from app.api.v1 import routes_health, routes_users

app = FastAPI(title="Learn FastAPI", version="1.0.0")


app.include_router(routes_health.router, prefix="/api/v1")
app.include_router(routes_users.router, prefix="/api/v1")


@app.get("/", tags=["root"])
def root():
    return {"message": "Hello world"}
