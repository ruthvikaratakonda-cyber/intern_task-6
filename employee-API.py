from fastapi import APIRouter

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.get("/")
def get_employees():
    return {"message": "List Employees"}

@router.post("/")
def create_employee():
    return {"message": "Employee Created"}