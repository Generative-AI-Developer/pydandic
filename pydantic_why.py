
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("inserted successfully.")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Updated successfully.")


patient_info = {"name": "Asif","age": 30}
patient_data = Patient(**patient_info)    
insert_patient_data(patient_data)
update_patient_data(patient_data)


