from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId

def create_connection():
    client = None
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["school"]
        print("Connection to MongoDB successful")
    except ConnectionFailure as e:
        print(f"The error '{e}' occurred")
    return db

def create_student(db, name, age, grade):
    collection = db["students"]
    student = {"name": name, "age": age, "grade": grade}
    try:
        collection.insert_one(student)
        print("Student created successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")

def get_students(db):
    collection = db["students"]
    try:
        students = list(collection.find())
        for student in students:
            student["_id"] = str(student["_id"])  # Convert ObjectId to string
        return students
    except Exception as e:
        print(f"The error '{e}' occurred")
        return []


    
# def get_student_by_id(db, student_id):
#     collection = db["students"]
#     try:
#         student = collection.find_one({"_id": ObjectId(student_id)})
#         return student
#     except Exception as e:
#         print(f"The error '{e}' occurred")
#         return None

def get_student_by_id(db, student_id):
    collection = db["students"]
    try:
        student = collection.find_one({"_id": ObjectId(student_id)})
        if student:
            # Convert ObjectId to string
            student['_id'] = str(student['_id'])
        return student
    except Exception as e:
        print(f"The error '{e}' occurred")
        return None

    
def update_student(db, student_id, name, age, grade):
    collection = db["students"]
    query = {"_id": ObjectId(student_id)}
    new_values = {"$set": {"name": name, "age": age, "grade": grade}}
    try:
        collection.update_one(query, new_values)
        print("Student updated successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")

def delete_student(db, student_id):
    collection = db["students"]
    query = {"_id": ObjectId(student_id)}
    try:
        collection.delete_one(query)
        print("Student deleted successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")
