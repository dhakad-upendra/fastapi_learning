
#nested model in pydantic

from pydantic import BaseModel, EmailStr, model_validator ,  Field, computed_field

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: int



class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_info = {'street': 'chor gali', 'city': 'delhi', 'state': 'NCR', 'zip_code': 450045}    
patient_info = {'name': 'John Doe', 'gender': 'Male', 'age': 30, 'address': Address(**address_info)}

patient1 = Patient(**patient_info)

print(patient1)
print(patient1.address.city)
print(patient1.address.zip_code)
print(patient1.address.state)

#exporting the pydantic model to in python dictionary format.
temp = patient1.model_dump()

print(temp)
print(type(temp))

temp1 = patient1.model_dump_json()

print(temp1)
print(type(temp1))

temp2 = patient1.model_dump(include={'name', 'age'})
#include and exclude are used to specify which fields to include or exclude when dumping the model. Here we are including only the name and age fields in the output dictionary.

print(temp2)
print(type(temp2))

temp3 = patient1.model_dump(exclude={'address':['state']})

print(temp3)
print(type(temp3))