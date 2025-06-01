from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    wieght: float
    hight: float 
    married: bool
    alergies: Optional[List[str]] 
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.wieght / (self.hight ** 2),2)
        return bmi

 
        

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.wieght)
    print(patient.married)
    print('BMI',patient.bmi)
    print(patient.alergies)
    print(patient.contact_details)
    


patient_info = {"name": "Asif","age": 30,"email":"abc@abl.com", "website":"https://www.google.com", "wieght": 72.5, "hight": 1.72, "married": True,
                "alergies": ["pollen", "dust"],
                "contact_details": {"email": "abc@gmail.com", "phone": "1234567890"}}


patient_data = Patient(**patient_info)    
insert_patient_data(patient_data)