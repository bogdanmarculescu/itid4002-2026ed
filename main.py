from fastapi import FastAPI
from sample_data import SAMPLE_RESPONSES
from domain.models import Employee

app = FastAPI(title="Running Example API")

EMPLOYEES = SAMPLE_RESPONSES

@app.get("/")
async def root():
    return {"message": "Welcome to ITID 4002 - Programming for Managers"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/employees/all", response_model=list[Employee])
async def get_employee_all():
    return EMPLOYEES


@app.get("/employees/{employee_id}")
async def get_employee(employee_id: str):
    for employee in EMPLOYEES:
        #if[employee.get("employee_id") == employee_id]:
        if [employee.employee_id == employee_id]:
            return employee