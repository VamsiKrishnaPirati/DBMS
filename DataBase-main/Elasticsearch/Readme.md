# Implementing CRUD Operations with Elastic Search and FastAPI

**Step-1**
1. Install Elastic Search
2. configure the server address as 127.0.0.1
3. Create table called students via kibana (install kibana also)

**Step-2**
1. Download main.py and database.py from elastic search folder
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
use the below commands in postman  
1. Open the postman application and use the below commands for operation
2. commands   
   **Get All**  
    curl -X 'GET' \  
      'http://127.0.0.1:8000/students/' \    
      -H 'accept: application/json'  
    
    **new record**  
    curl -X 'PUT' \  
      'http://127.0.0.1:8000/students/1/' \  
      -H 'accept: application/json' \  
      -H 'Content-Type: application/json' \  
      -d '{  
      "name": "nagendra",  
      "age": 11,  
      "grade": "A+"  
    }'
   
    **Get by id**  
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
