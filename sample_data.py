"""Three hard-coded entries copied from data/org_health_survey.csv (demo/test data)."""
from domain.models import Employee

SAMPLE_RESPONSES = [
    Employee(
        employee_id="EMP0001",
        division="Division 1",
        tenure_years=10.4,
        role_type="Blue collar",
        role_level="Senior operator",
        shift="Night",
        union_member=False,
    ),
    Employee(
        employee_id="EMP0002",
        division="Division 1",
        tenure_years=6.9,
        role_type="Blue collar",
        role_level="Operator",
        shift="Night",
        union_member=True,
    ),
    Employee(
        employee_id="EMP0003",
        division="Division 1",
        tenure_years=6.4,
        role_type="Blue collar",
        role_level="Operator",
        shift="Afternoon",
        union_member=False,
    ),
    Employee(
        employee_id="EMP0001",
        division= "Division 1",
        tenure_years= 10.4,
        role_type= "Blue collar",
        role_level= "Senior operator",
        shift= "Night",
        union_member=False
    ),
    Employee(
        employee_id="EMP0018",
        division= "Division 1",
        tenure_years= 6.2,
        role_type= "White collar",
        role_level= "Specialist",
        shift= "Night",
        union_member=False
    ),
    Employee(
        employee_id="EMP0346",
        division= "Division 2",
        tenure_years= 20.3,
        role_type= "White collar",
        role_level= "Specialist",
        shift= "Day (office)",
        union_member=True
    )
]
