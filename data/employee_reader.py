import csv
from pathlib import Path
from model.employee import Employee

def read_employees(filename: str) -> list[Employee]:
    employees = []

    data_dir = Path(__file__).resolve().parent
    file_path = data_dir / filename

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employee = Employee(
                employee_id = row["employee_id"],
                division = row["division"],
                tenure_years = float(row["tenure_years"]),
                role_type = row["role_type"],
                role_level = row["role_level"],
                shift = row["shift"],
                union_member = bool(row["union_member"]),
            )
            employees.append(employee)
    return employees