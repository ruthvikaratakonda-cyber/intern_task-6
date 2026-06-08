from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.post("/checkin")
def check_in(employee_id: int):

    return {
        "employee_id": employee_id,
        "checkin": datetime.now()
    }

@router.post("/checkout")
def check_out(employee_id: int):

    return {
        "employee_id": employee_id,
        "checkout": datetime.now()
    }