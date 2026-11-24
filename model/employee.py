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

@dataclass
class Survey_Entry:
    A1_free_to_decide: int
    A2_manager_gives_choice: int
    A3_pressured_rev: int
    A4_feel_capable: int
    A5_have_skills: int
    A6_rarely_succeed_rev: int
    A7_feel_i_belong: int
    A8_colleagues_care: int
    A9_feel_isolated_rev: int
    A10_work_meaningful: int
    A11_work_because_have_to_rev: int
    B1_purposeful_work_life: int
    B2_competent_capable: int
    B3_engaged_daily_tasks: int
    B4_relationships_rewarding: int
    B5_optimistic_future: int
    B6_feel_positive_energized: int
    B7_feel_stressed_rev: int
    B8_feel_content_satisfied: int
    B9_feel_exhausted_rev: int
    B10_sense_of_belonging: int
    B11_feel_job_secure: int
    C1_clear_targets: int
    C2_useful_feedback: int
    C3_poor_perf_addressed: int
    C4_recognized_rewarded: int
    C5_workload_manageable: int
    C6_training_access: int
    C7_career_path_visible: int
    E1_physically_safe: int
    E2_psych_safe_speak_up: int
    E3_manager_takes_safety_seriously: int

