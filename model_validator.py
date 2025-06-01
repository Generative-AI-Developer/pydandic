from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    wieght: float
    married: bool
    alergies: Optional[List[str]] 
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        return model
        

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.wieght)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)
    


patient_info = {"name": "Asif","age": 65,"email":"abc@abl.com", "website":"https://www.google.com", "wieght": 70.5, "married": True,
                "alergies": ["pollen", "dust"],
                "contact_details": {"email": "abc@gmail.com", "phone": "1234567890","emergency": "9876543210"}}


patient_data = Patient(**patient_info)    
insert_patient_data(patient_data)