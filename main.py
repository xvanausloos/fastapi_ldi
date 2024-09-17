from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, {"title": "favorite foods", "content": "I like pizza", "id":2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    print(f"latest id = {post}")
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
    return post

# change by xav in main branch done in GH directly
