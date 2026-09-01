
from fastapi import FastAPI, Path,HTTPException
import json
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Patient Management System"}
@app.get("/about")
def about():
    return {"message": "Management system for patients, doctors, and appointments."}

#to load data form json file  i willl cretate a function 
def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

#show all patients
@app.get('/view')
def view_patients():
    datas= load_data()
    return datas

@app.get('/view/{patient_id}')
def view_patient(patient_id: str = Path(..., description="ID of patient",example="P001")):
    datas= load_data()
    if patient_id in datas :
        return datas[patient_id]
    else:
        raise HTTPException(status_code=404,detail = "Patient not found.")
     