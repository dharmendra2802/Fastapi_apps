from pydantic import BaseModel

class PostItem(BaseModel):
    title: str
    content: str
