
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50,title="Name of Patient", description="Name of the patient must be between 3 and 50 characters")]
    email: EmailStr
    website: AnyUrl
    age: int = Field(..., ge=0, le=120, description="Age of the patient must be between 0 and 120")
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

    print("Updated successfully.")



patient_info = {"name": "Asif","age": 30,"email":"abc@gmail.com", "website":"https://www.google.com", "wieght": 70.5, "married": True,
                "alergies": ["pollen", "dust"],
                "contact_details": {"email": "abc@gmail.com", "phone": "1234567890"}}


patient_data = Patient(**patient_info)    
insert_patient_data(patient_data)
update_patient_data(patient_data)


