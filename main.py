from fastapi import FastAPI

app = FastAPI()


EMPLOYEES = [
    {"id": 1, "name": "Bogdan", "happy": 5},
    {"id": 2, "name": "Knut-Eric", "happy": 7},
]

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