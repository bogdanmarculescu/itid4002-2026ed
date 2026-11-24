from typing import Optional

from model.employee import Employee
from data.employee_reader import read_employees

def get_all_employees():
    return read_employees()

def get_employee_by_id(employee_id: str) -> Optional[Employee]:
    all_employees = read_employees()

    for employee in all_employees:
        if employee.employee_id == employee_id:
            return employee

def get_employee_tenured_less_than(tenure: float):
    all_employees = read_employees()
    result = []

    for employee in all_employees:
        if employee.tenure_years < tenure:
            result.append(employee)
    return result

def get_employee_tenured_greater_than(tenure: float):
    all_employees = read_employees()
    result = []

    for employee in all_employees:
        if employee.tenure_years > tenure:
            result.append(employee)
    return result
