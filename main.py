from fastapi import FastAPI
from data.employee_data_reader import read_employee_data

app = FastAPI()


EMPLOYEES = read_employee_data()

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
    result = []
    for employee in EMPLOYEES:
        if level > employee["happy"]:
            result.append(employee)
    return result

