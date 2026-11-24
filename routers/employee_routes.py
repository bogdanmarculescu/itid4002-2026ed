from fastapi import APIRouter
from services.employee_service import (
    get_all_employees,
    get_employee_by_id,
    get_employee_tenured_less_than
)

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)

@router.get("/all")
def all_employees():
    return get_all_employees()

@router.get("/id/{employee_id}")
def employee(employee_id: str):
    return get_employee_by_id(employee_id)

@router.get("tenured_less/{tenure}")
def employee_tenure_less(tenure: float):
    return get_employee_tenured_less_than(tenure)