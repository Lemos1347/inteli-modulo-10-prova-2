from pydantic import BaseModel


class BlogCreationInputDTO(BaseModel):
    id: int
    title: str
    content: str


class BlogEditInputDTO(BaseModel):
    title: str
    content: str
