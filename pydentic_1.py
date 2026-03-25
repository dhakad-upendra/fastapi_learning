from pydantic import BaseModel, Field , AnyUrl, EmailStr, field_validator
from typing import List, Dict, Optional, Annotated




class patient(BaseModel):
    name: str
    age: int
    weight: Annotated[float, Field(gt=0, description="Weight must be greater than 0")] #this is validating that weight should be a positive float   
    married: bool
    allergies:Optional[List[str]] = None #this is validating that allergies should be a list of strings
    #optional is used to make the allergies field optional, meaning it can be omitted when creating a patient object. If provided, it must be a list of strings.

    contact_info: Dict [str, str] #this is validating that contact_info should be a dictionary with string keys and string values


#field validator is used to validate the fields of a pydentic model. Here we are validating whether the email is of a valid bank domain or not...

    @field_validator('email')
    @classmethod
    def validate_email( cls, value):
        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']
        domain = value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}")
        return value


    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        return value.upper() 
    #this is validating that the name should be in uppercase letters. The value.upper() method converts the input name to uppercase before returning it.
    
    




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

