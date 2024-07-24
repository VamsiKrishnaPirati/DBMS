from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize FAISS index
dimension = 384  # Dimension of the embeddings produced by the model
index = faiss.IndexFlatL2(dimension)  # Base index (L2 distance)
id_index = faiss.IndexIDMap(index)  # Index to map IDs to vectors
id_to_text: Dict[int, str] = {}  # Dictionary to map IDs to original text
next_id = 0  # Initialize ID counter

class TextItem(BaseModel):
    text: str

class TextItems(BaseModel):
    texts: List[str]

class UpdateTextItem(BaseModel):
    id: int
    text: str

class DeleteTextItem(BaseModel):
    id: int

@app.post("/create")
def create_texts(items: TextItems):
    global next_id
    embeddings = model.encode(items.texts)  # Generate embeddings
    ids = list(range(next_id, next_id + len(items.texts)))
    id_index.add_with_ids(embeddings, np.array(ids))  # Add embeddings with IDs to the FAISS index
    for i, text in zip(ids, items.texts):
        id_to_text[i] = text
    next_id += len(items.texts)
    return {"ids": ids, "embeddings": embeddings.tolist()}

@app.get("/read/{item_id}")
def read_text(item_id: int):
    if item_id not in id_to_text:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "text": id_to_text[item_id]}

@app.put("/update")
def update_text(item: UpdateTextItem):
    if item.id not in id_to_text:
        raise HTTPException(status_code=404, detail="Item not found")
    # Remove old embedding
    id_index.remove_ids(np.array([item.id]))
    # Add new embedding
    new_embedding = model.encode([item.text])
    id_index.add_with_ids(new_embedding, np.array([item.id]))
    id_to_text[item.id] = item.text
    return {"id": item.id, "new_embedding": new_embedding.tolist()}

@app.delete("/delete")
def delete_text(item: DeleteTextItem):
    if item.id not in id_to_text:
        raise HTTPException(status_code=404, detail="Item not found")
    # Remove embedding
    id_index.remove_ids(np.array([item.id]))
    del id_to_text[item.id]
    return {"id": item.id, "message": "Deleted successfully"}

@app.get("/read_all")
def read_all_texts():
    all_texts = [{"id": item_id, "text": text} for item_id, text in id_to_text.items()]
    return all_texts
