from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    wieght: float
    married: bool
    alergies: Optional[List[str]] 
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        

        valid_domains = ["abl.com", "mcb.com", "hbl.com"]
        domain_name = value.split('@')[-1]
        print(f"Domain Name: {domain_name}")
        if domain_name not in valid_domains:
            raise ValueError("Not a valid Domain Name")
        return value
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
    
        return value.upper()

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.wieght)
    print(patient.married)
    print(patient.alergies)
    print(patient.contact_details)
    


patient_info = {"name": "Asif","age": 30,"email":"abc@abl.com", "website":"https://www.google.com", "wieght": 70.5, "married": True,
                "alergies": ["pollen", "dust"],
                "contact_details": {"email": "abc@gmail.com", "phone": "1234567890"}}


patient_data = Patient(**patient_info)    
insert_patient_data(patient_data)