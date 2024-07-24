from elasticsearch import Elasticsearch, exceptions as es_exceptions
from elasticsearch.helpers import bulk

# Initialize Elasticsearch connection
def create_connection():
    es = None
    try:
        es = Elasticsearch([{'host': '127.0.0.1', 'port': 9200, 'scheme': 'http'}])
        if es.ping():
            print("Connection to Elasticsearch successful")
        else:
            print("Elasticsearch cluster is down!")
    except es_exceptions.ConnectionError as e:
        print(f"Connection failed: {e}")
    return es

# Function to create a student document
def create_student(es, name, age, grade):
    student_document = {
        'name': name,
        'age': age,
        'grade': grade
    }
    try:
        res = es.index(index='students', body=student_document)
        print(f"Student created successfully. ID: {res['_id']}")
    except es_exceptions.RequestError as e:
        print(f"Error creating student: {e}")

# Function to retrieve all students
def get_students(es):
    try:
        res = es.search(index='students', size=1000)
        students = [hit['_source'] for hit in res['hits']['hits']]
        return students
    except es_exceptions.RequestError as e:
        print(f"Error retrieving students: {e}")
        return []

# Function to retrieve a student by ID
def get_student_by_id(es, student_id):
    try:
        res = es.get(index='students', id=student_id)
        if res['found']:
            return res['_source']
        else:
            return None
    except es_exceptions.NotFoundError:
        return None
    except es_exceptions.RequestError as e:
        print(f"Error retrieving student: {e}")
        return None

# Function to update a student document
def update_student(es, student_id, name, age, grade):
    student_document = {
        'name': name,
        'age': age,
        'grade': grade
    }
    try:
        res = es.index(index='students', id=student_id, body=student_document)
        print(f"Student updated successfully. ID: {res['_id']}")
    except es_exceptions.RequestError as e:
        print(f"Error updating student: {e}")

# Function to delete a student by ID
def delete_student(es, student_id):
    try:
        res = es.delete(index='students', id=student_id)
        print(f"Student deleted successfully. ID: {student_id}")
    except es_exceptions.RequestError as e:
        print(f"Error deleting student: {e}")
