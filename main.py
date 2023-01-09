from operator import pos
from urllib import response
from fastapi import Body, FastAPI, HTTPException, status
from pydantic import BaseModel
from random import randrange 

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

my_posts = [{"title": "All about me", "content": "My name and age", "id": 1}, {"title": "Likes and dislikes", "Favourite things":
"food, babies, kind people", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Welcome to my first api! tadaa..."}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):    
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} not found")
    return {"info": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_post_index(id)
    my_posts.pop(index)
    return {"message": "post deleted successfully"}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} not found")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}

 


