from dataclasses import dataclass


@dataclass
class Employee:
    employee_id: str
    division: str
    tenure_years: float
    role_type: str
    role_level: str
    shift: str
    union_member: bool