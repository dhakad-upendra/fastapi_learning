from fastapi import FastAPI , Path , HTTPException
import json

app = FastAPI()

def load_patients():
    with open('data.json', 'r') as f:
        patients = json.load(f)
    return patients


@app.get('/')
def hello():
    return {"message": "Patient management system API"}

@app.get('/about')
def about():
    return {"message": "A simple API for managing patient records in a healthcare system."}



@app.get('/view')
def view():
    patients = load_patients()
    return patients


@app.get('/view/{patient_id}')
def view_patient(patient_id: str = Path(..., description = "The Id of the patient to view" , example = "P001")):
        data = load_patients()
        if patient_id in data:
             return data[patient_id]
        raise HTTPException(status_code = 404, detail = "Patient not found")
