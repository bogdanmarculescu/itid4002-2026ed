import csv
from pathlib import Path

from model.employee import Employee

def read_employee_data() -> list[Employee]:
    # some code to read from the file

    data_dir = Path(__file__).parent

    filename = 'org_health_survey.csv'
    file_path = data_dir / filename
    result = []

    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            emp = Employee(
                employee_id=row['employee_id'],
                division=row['division'],
                tenure_years=float(row['tenure_years']),
                role_level=row['role_level'],
                role_type=row['role_type'],
                shift=row['shift'],
                union_member=bool(row['union_member']),
            )
            result.append(emp)
            #employees.append(Employee(row))

    # some definition of what I expect in return
    # -> list employees

    return result
