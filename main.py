
from fastapi import FastAPI, Path,HTTPException,Query
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
@app.get("/sort")
def  sor_patients(sort_by: str = Query(...,description="Sort patients by height,weight or age", example="height"),order: str = Query('asc',description="Sort in ascending order")):
    valid_sort_by = ['height', 'weight', 'age']
    if sort_by not in valid_sort_by:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of {valid_sort_by}.") #400 mane client teke vul
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order value. Must be 'asc' or 'desc'.")
    data = load_data()
    sort_order = True if order != 'asc' else False
    
    sorted_data=sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    return sorted_data

