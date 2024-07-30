from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

@app.get("/about")
def index():
    return {'data':{
        "name":"alpha",
        "age":"",
        #"id":id
    }}
    
@app.get("/blog/{id}")
def show(id:str):
    return {'data':id}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"Blog is created with title as {blog.title}"}