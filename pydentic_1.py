from pydantic import BaseModel
from typing import List, Dict
class patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_info: Dict [str, str]




patient_info = {'name': 'human', 'age': 23, 'weight': 70.5, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_info': {'email':'human@example.com'}}


patient_obj = patient(**patient_info)  # ** used to unpacking the dictionary into keyword arguments

def get_patient_info(patient: patient): #we are giving patient obj of datatype patient defined by pydantic model
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)

    return patient

print(get_patient_info(patient_obj))

