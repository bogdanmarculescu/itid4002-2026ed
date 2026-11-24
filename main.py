import os
from fastapi import FastAPI
from data.employee_reader import read_employees

app = FastAPI()



print("Current working directory:", os.getcwd())

EMPLOYEES = read_employees("org_health_survey.csv")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/employees")
async def get_employees():
    return {"employees": EMPLOYEES}

@app.get("/employees/happy/{level}")
async def get_employee(level: int):

    for employee in EMPLOYEES:
        if level > employee["happy"]:
            return employee