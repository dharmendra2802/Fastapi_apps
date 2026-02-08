from fastapi import FastAPI, HTTPException
from .db import Post, create_db_and_tables, get_async_session
from .schema import PostItem
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)

text_posts = {1: {"title": "First post", "content": "Content of first post"}, 2: {"title": "Second post", "content": "Content of second post"}, 3: {"title": "Third post", "content": "Content of third post"}, 4: {"title": "Fourth post", "content": "Content of fourth post"}, 5: {"title": "Fifth post", "content": "Content of fifth post"}, 6: {"title": "Sixth post", "content": "Content of sixth post"}, 7: {"title": "Seventh post", "content": "Content of seventh post"}, 8: {"title": "Eighth post", "content": "Content of eighth post"}, 9: {"title": "Ninth post", "content": "Content of ninth post"}, 10: {"title": "Tenth post", "content": "Content of tenth post"}}


@app.get("/")
def main():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/posts")
def get_all_posts(limit:int = None):
    if limit:
        return { i:j for i ,j in  text_posts.items() if i <= limit}
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id, "Post not found")   

@app.post("/posts")
def create_post(post: PostItem):
    post_id = max(text_posts.keys()) + 1
    text_posts[post_id] = {"title": post.title, "content": post.content}
    return {"message": "Post created successfully", "post": {"id": post_id, "title": post.title, "content": post.content}}