from pydantic import BaseModel, EmailStr, model_validator ,  Field, computed_field
from typing import List, Dict, Optional, Annotated



class patient(BaseModel):
    name: str
    age: int
    weight: Annotated[float, Field(gt=0, description="Weight must be greater than 0")] #this is validating that weight should be a positive float  
    height: Annotated[float, Field(gt=0, description="Height must be greater than 0")] #this is validating that height should be a positive float

    married: bool
    allergies:Optional[List[str]] = None #this is validating that allergies should be a list of strings
    #optional is used to make the allergies field optional, meaning it can be omitted when creating a patient object. If provided, it must be a list of strings.

    contact_info: Dict [str, str] #this is validating that contact_info should be a dictionary with string keys and string values


    @model_validator(mode='before')
    def validate_emergency_contact(cls, model):
        if isinstance(model, dict) and model.get('age',0)> 60 and not model.get('emergency_contact'):
            raise ValueError("Emergency contact is required for patients above 60 years old.")
        return model


    @computed_field  #computed_field is used to define a field that is computed based on other fields in the model. Here we are computing the BMI (Body Mass Index) based on the weight and height of the patient.  
    
    @property
    def bmi(self) -> float:
        bmi =round(self.weight / (self.height ** 2),2)
        return bmi     


patient_info = {'name': 'human', 'age': 23, 'weight': 70.5,'height':1.70, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_info': {'email':'human@example.com'}}

patient_obj = patient(**patient_info)  # ** used to unpacking the dictionary into keyword arguments

print(patient_obj.bmi) 