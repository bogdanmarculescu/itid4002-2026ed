# Hello API
 
## Setup
    python -m venv .venv
    source .venv/bin/activate      # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

    .venv/bin/python -m uvicorn --version.venv/bin/python -m pip install -r requirements.txt 
 
## Run
    uvicorn main:app --reload
 
## Try it
- http://127.0.0.1:8000/hello/Bogdan
- http://127.0.0.1:8000/employees/happy/7
- Interactive docs: http://127.0.0.1:8000/docs
 