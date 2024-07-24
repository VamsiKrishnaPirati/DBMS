from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bson.objectid import ObjectId

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

db = create_connection()

# Define Pydantic BaseModel for Student
class Student(BaseModel):
    name: str
    age: int
    grade: str

# FastAPI endpoints
@app.post("/students/", response_model=dict)
def api_create_student(student: Student):
    create_student(db, student.name, student.age, student.grade)
    return {"message": "Student created successfully"}

@app.get("/students/", response_model=list)
def api_get_students():
    students = get_students(db)
    return students

@app.get("/students/{student_id}", response_model=dict)
def api_get_student(student_id: str):
    student = get_student_by_id(db, ObjectId(student_id))
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=dict)
def api_update_student(student_id: str, student: Student):
    update_student(db, ObjectId(student_id), student.name, student.age, student.grade)
    return {"message": "Student updated successfully"}

@app.delete("/students/{student_id}", response_model=dict)
def api_delete_student(student_id: str):
    delete_student(db, ObjectId(student_id))
    return {"message": "Student deleted successfully"}
