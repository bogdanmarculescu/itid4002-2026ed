from fastapi import FastAPI
from routers.employee_routes import router as employee_router
app = FastAPI(
    title="Employee Demo",
    version="1.0",
)

app.include_router(employee_router)