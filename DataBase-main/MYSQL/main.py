from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import (
    create_connection,
    create_student,
    get_students,
    get_student_by_id,
    update_student,
    delete_student,
)

# Initialize FastAPI app
app = FastAPI()

connection = create_connection()

# Define Pydantic BaseModel for Student
class Student(BaseModel):
    name: str
    age: int
    grade: str

# FastAPI endpoints (assuming these are unchanged)
@app.post("/students/", response_model=dict)
def api_create_student(student: Student):
    create_student(connection, student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/students/", response_model=list)
def api_get_students():
    students = get_students(connection)
    return students

@app.get("/students/{student_id}", response_model=dict)
def api_get_student(student_id: int):
    student = get_student_by_id(connection, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=dict)
def api_update_student(student_id: int, student: Student):
    update_student(connection, student_id, student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}", response_model=dict)
def api_delete_student(student_id: int):
    delete_student(connection, student_id)
    return {"message": "Student deleted successfully"}