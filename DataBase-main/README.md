# DataBase
## Implementing CRUD Operations with MySQL and FastAPI

**Step-1**
MYSQL WorkBench
1. Create a local Connection in MYSQL with
   userid: root
   password: 123456
2. Create a database school
   command: create database school;
   command: use school;
3. create a table called students
   command:
   CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(10) NOT NULL
    );


**Step-2** Setup
1. Download the main.py and database.py files from the MYSQL folder
2. Keep the both files in a same folder
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

    **Create an entry**  
    curl -X 'POST' \
      'http://127.0.0.1:8000/students/' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "name": "string",
      "age": 0,
      "grade": "string"
    }'
    
    **Get by unique id**  
    curl -X 'GET' \
      'http://127.0.0.1:8000/students/1' \
      -H 'accept: application/json'
    
    **Update**  
    curl -X 'PUT' \
      'http://127.0.0.1:8000/students/1' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "name": "string",
      "age": 0,
      "grade": "string"
    }'
    
    **Delete**  
    curl -X 'DELETE' \
      'http://127.0.0.1:8000/students/1' \
      -H 'accept: application/json'


## Implementing CRUD Operations with MongoDB and FastAPI  

**Step-1**  
Install MongoDB in your system and follow below steps  
1. Open Command prompt
2. Use commands below    
   mongosh (initilizing the mongodb)  
   show dbs (check what databases are available)  
   use school (create school database if not available else it will use school database)   

**Step-2**  setup
1. Download the main.py and database.py files from the MongoDB folder
2. Keep the both files in a same folder
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
   **Create**     
   curl -X POST "http://localhost:8000/students/" -H "Content-Type: application/json" -d '{"name": "Mukesh", "age": 20, "grade": "A"}'

   **get all**  
   curl -X GET http://localhost:8000/students/
   
   **get by student id**    
   curl -X GET http://localhost:8000/students/6692885566301ae0123b0d7b

   **update student id**     
   curl -X PUT "http://localhost:8000/students/6692885566301ae0123b0d7b" -H "Content-Type: application/json" -d '{"name": "nagendra", "age": 21, "grade": "B"}'  
   or  
   curl -X PUT "http://localhost:8000/students/669272b27c418869ffc4e49c" \  
   -H "Content-Type: application/json" \  
   -d '{"name": "nagendra", "age": 21, "grade": "B"}'  

   **Delete student**     
   curl -X DELETE http://localhost:8000/students/6692885566301ae0123b0d7b


# Implementing CRUD Operations with Elastic Search and FastAPI
   
See the read me file in elastic search folder
























