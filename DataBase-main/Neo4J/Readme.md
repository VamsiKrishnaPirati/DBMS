
# Implementing CRUD Operations with MySQL and FastAPI

**Step-1**
Neo4J WorkBench
1. Create a local Connection in Neo4J with
   userid: root
   password: 12345678

**Step-2** Setup
1. Download the main.py and database.py and test.py files from the neo4J folder
2. Keep the all files in a same folder
3. Open in VS studio and select the desired folder (set path)
4. run the python terminal
5. initiate the fastapi (run)  
   Command :  
   uvicorn main:app --reload  
   or  
   fastapi dev main.py
6. FASTAPI connection is established

**Step-3**
Test the application
1. Open the postman application and use the below commands for operation
2. Commands  
   **Get Command**  
    curl -X 'GET' \  
    'http://127.0.0.1:8000/students/' \   
    -H 'accept: application/json'  

    **Get by ID**  
    curl -X 'GET' \  
    'http://127.0.0.1:8000/students/1' \  
    -H 'accept: application/json'  



    **Create an entry**  
    curl -X 'POST' \  
    'http://127.0.0.1:8000/students/' \  
    -H 'accept: application/json' \  
    -H 'Content-Type: application/json' \  
    -d '{  
    "student_id": 1,  
    "name": "nagendra",  
    "age": 22,  
    "grade": "A+"  
    }'  

    
    
    **Update**  
    curl -X 'PUT' \  
    'http://127.0.0.1:8000/students/1' \  
    -H 'accept: application/json' \  
    -H 'Content-Type: application/json' \  
    -d '{  
    "student_id": 1,  
    "name": "string",  
    "age": 0,  
    "grade": "string"  
    }'  

    
    **Delete**  
    curl -X 'DELETE' \  
    'http://127.0.0.1:8000/students/1' \  
    -H 'accept: application/json'  

