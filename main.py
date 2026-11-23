from fastapi import FastAPI

app = FastAPI(title="Running Example API")

EMPLOYEES = [
    {"EMP0001",	"Division 1",	10.4,	"Blue collar",	"Senior operator",	"Night",	"No",	3,	2,	2,	3,	3,	3,	2,	2,	4,	3,	3,	3,	2,	3,	3,	4,	1,	4,	2,	4,	3,	4,	3,	2,	3,	2,	1,	1,	2,	1,	2,	2,	"drag",	"v2_org_wide"},
    {"EMP0018",	"Division 1",	6.2, "White collar",	"Specialist",	    "Night",	"No",	1,	1,	4,	4,	2,	2,	2,	2,	3,	1,	4,	1,	5,	4,	1,	2,	1,	5,	1,	5,	2,	3,	3,	2,	2,	2,	2,	3,	3,	3,	3,	3,	"drag",	"v2_org_wide"},
    {"EMP0346",	"Division 2",	20.3,	"White collar",	"Specialist",	"Day (office)",	"Yes",	1,	1,	5,	2,	2,	4,	3,	3,	4,	2,	5,	3,	3,	2,	2,	2,	3,	3,	3,	2,	4,	3,	3,	3,	2,	3,	3,	3,	2,	5,	4,	3,	"drag",	"v2_org_wide"}


]

@app.get("/")
async def root():
    return {"message": "Welcome to ITID 4002 - Programming for Managers"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/employees/{employee_id}")
async def get_employee(employee_id: str):
    for employee in EMPLOYEES:
        if["employee_id"] == employee_id:
            return employee