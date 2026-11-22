"""The two data structures of the API.

Employee      - who the person is (profile data).
SurveyAnswers - what the person answered (one score per survey item).

Both are linked by `employee_id`. They are plain dataclasses; FastAPI can
return them directly as JSON.
"""
from dataclasses import dataclass


@dataclass(frozen=True)  # frozen = read-only once created
class Employee:
    employee_id: str
    division: str
    tenure_years: float
    role_type: str       # e.g. 'Blue collar' / 'White collar'
    role_level: str      # e.g. 'Operator', 'Team lead'
    shift: str           # e.g. 'Morning', 'Night'
    union_member: bool


@dataclass(frozen=True)
class SurveyAnswers:
    # One field per survey item, named like the CSV column but lowercase.
    # Scores are stored exactly as in the CSV. Items ending in `_rev` are
    # reverse-worded questions and are NOT re-coded here.
    employee_id: str

    # Section A
    a1_free_to_decide: int
    a2_manager_gives_choice: int
    a3_pressured_rev: int
    a4_feel_capable: int
    a5_have_skills: int
    a6_rarely_succeed_rev: int
    a7_feel_i_belong: int
    a8_colleagues_care: int
    a9_feel_isolated_rev: int
    a10_work_meaningful: int
    a11_work_because_have_to_rev: int

    # Section B
    b1_purposeful_work_life: int
    b2_competent_capable: int
    b3_engaged_daily_tasks: int
    b4_relationships_rewarding: int
    b5_optimistic_future: int
    b6_feel_positive_energized: int
    b7_feel_stressed_rev: int
    b8_feel_content_satisfied: int
    b9_feel_exhausted_rev: int
    b10_sense_of_belonging: int
    b11_feel_job_secure: int

    # Section C
    c1_clear_targets: int
    c2_useful_feedback: int
    c3_poor_perf_addressed: int
    c4_recognized_rewarded: int
    c5_workload_manageable: int
    c6_training_access: int
    c7_career_path_visible: int

    # Section E
    e1_physically_safe: int
    e2_psych_safe_speak_up: int
    e3_manager_takes_safety_seriously: int