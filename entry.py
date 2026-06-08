from fastapi import FastAPI
from app.api import employee, department, attendance, auth

app = FastAPI(
    title="Enterprise Employee Management System",
    version="1.0"
)

app.include_router(auth.router)
app.include_router(employee.router)
app.include_router(department.router)
app.include_router(attendance.router)

@app.get("/")
def home():
    return {"message": "Enterprise Employee Management System"}


































