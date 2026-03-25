from fastapi import FastAPI , Path , HTTPException, Query
import json
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field , computed_field
from typing import List, Dict, Optional, Annotated, Literal

app = FastAPI()

class Patient(BaseModel):

    id : Annotated[str, Field(..., description="The ID of the patient", examples=['P001'])]
    name: Annotated[str, Field(..., description="The name of the patient", examples=['John Doe'])]
    city: Annotated[str, Field(..., description="The city of the patient", examples=['Delhi'])]
    age: Annotated[int, Field(..., description="The age of the patient", examples=[30])]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="The gender of the patient")]
    height : Annotated[float, Field(..., gt =0, description="The height of the patient in meters", examples=[1.75])]
    weight : Annotated[float, Field(..., gt =0,  description="The weight of the patient in kilograms", examples=[70.0])]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"





def load_patients():
    with open('data.json', 'r') as f:
        patients = json.load(f)
    return patients

def save_patients(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)


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



@app.post('/create')
def create_patient(patient: Patient):
     
     #load the existing data
    data = load_patients()

    #check if the patient ID already exists
    if patient.id in data:
        raise HTTPException(status_code = 400, detail = "Patient with this ID already exists")
    
    # new patient data to be added

    data[patient.id] = patient.model_dump(exclude={'id'})

    #save the data back to the file

    save_patients(data)

    return JSONResponse(content={"message": "Patient created successfully"}, status_code = 201)