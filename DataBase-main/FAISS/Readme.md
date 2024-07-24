# Implementing CRUD Operations with FAISS and FastAPI

**Step-1** Setup
1. Download the main.py  files from the FAISS folder
2. Open in VS studio and select the desired folder (set path)
3. run the python terminal
4. initiate the fastapi (run)  
   Command :  
   uvicorn main:app --reload  
   or  
   fastapi dev main.py
5. FASTAPI connection is established

**Step-2**
Test the application
1. Open the postman application and use the below commands for operation
2. Commands  
   **Get Command**  
    curl -X 'GET' \  
    'http://127.0.0.1:8000/read/1' \  
    -H 'accept: application/json'   


    **Create an entry**  
    curl -X 'POST' \  
    'http://127.0.0.1:8000/create' \  
    -H 'accept: application/json' \  
    -H 'Content-Type: application/json' \  
    -d '{  
    "texts": ["This is an example sentence.", "Each sentence is converted into embeddings."]  
    }'  


    **Update**  
    curl -X 'PUT' \  
    'http://127.0.0.1:8000/update' \  
    -H 'accept: application/json' \  
    -H 'Content-Type: application/json' \  
    -d '{  
    "id": 1,  
    "text": "Updated sentence."  
    }'  

    
    **Delete**  
    curl -X 'DELETE' \  
    'http://127.0.0.1:8000/delete' \  
    -H 'accept: application/json' \  
    -H 'Content-Type: application/json' \  
    -d '{  
    "id": 1  
    }'  

