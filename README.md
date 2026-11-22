# ITID 4002 - Programming for Managers

This repository contains the running example and relevant code for the course 
ITID4002 - Programming for Manager - 2026 edition - Kristiania University of Applied Sciences

## Introduction

The idea of the respository is to follow along with the course and the relevant code (with each lecture being a separate branch). The repository is to be used as a guide, in addition to the materials presented in class, in class participation in discussion, and all other relevant activities

[Startup Information](/Startup.md)



## Setup
    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
 
## Run
    uvicorn main:app --reload
 
## Try it
- http://127.0.0.1:8000/hello/Bogdan
- http://127.0.0.1:8000/employees/{employee_id}
- http://127.0.0.1:8000/employees/EMP001
- Interactive docs: http://127.0.0.1:8000/docs
 