
from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    wieght: float
    married: bool
    alergies: Optional[List[str]] = None
    contact_details: Dict[str, str]



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.wieght)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)
    

    print("inserted successfully.")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.wieght)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)


patient_info = {"name": "Asif","age": 30, "wieght": 70.5, "married": True,
                "alergies": ["pollen", "dust"],
                "contact_details": {"email": "abc@gmail.com", "phone": "1234567890"}}


patient_data = Patient(**patient_info)    
insert_patient_data(patient_data)
update_patient_data(patient_data)


