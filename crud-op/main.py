from fastapi import FastAPI,HTTPException
from models import Employee
from typing import List

employees_db: List[Employee] = []

app = FastAPI()

#1. Read All Employees
@app.get('/employees',response_model=List[Employee])
def get_employees():
    return employees_db

#2 Read specific employee
@app.get('/employees/{emp_id}',response_model=Employee)
def get_employee(empid:int):
    for employee in employees_db:
        if empid == employee.id:
            return employee
        
    raise HTTPException(status_code=404,detail="Employee NOT Found")

# 3. Add an employee
@app.post('/employees',response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400,detail='Employee already exists')
    employees_db.append(new_emp)
    return new_emp
    
# 4. Update an Employee
@app.put('/update_employee/{emp_id}')
def update_employee(emp_id: int, updated_emp: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_emp
            return updated_emp
    
    raise HTTPException(status_code=404, detail="Employee NOT Found")

# 5. Delete an Employee
@app.delete('/delete_employee/{emp_id}',response_model=Employee)
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {"detail": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee NOT Found")





