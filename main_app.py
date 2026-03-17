from fastapi import FastAPI , Path , HTTPException, Query
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

@app.get('/sort')
def sort_patients(sort_by: str = Query(... , description = "Sort on basis of height, weigth  or bmi"), order: str = Query('asc', description= 'sort in asc or desc order')):
     
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
            raise HTTPException(status_code = 400, detail = f"Invalid sort field. Must be one of {valid_fields}")
    
    if order not in ['asc', 'desc']:
            raise HTTPException(status_code = 400, detail = "Invalid sort order. Must be 'asc' or 'desc'")  
    
    data = load_patients()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by, 0), reverse = sort_order)

    return sorted_data