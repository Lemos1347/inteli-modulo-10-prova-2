import logging

from fastapi import FastAPI, Response, status
from src.schema import BlogCreationInputDTO
from src.schema.dtos import BlogEditInputDTO

app = FastAPI()

blog_posts = []

# logger = logging.getLogger()
# handler = logging.StreamHandler()
# file_handler = logging.FileHandler("logs.txt")
# formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)

level = logging.WARNING
format = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
handlers = [logging.FileHandler("logs.txt"), logging.StreamHandler()]

logging.basicConfig(level=level, format=format, handlers=handlers)


class BlogPost:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return f"{self.id} - {self.title} - {self.content}"

    def toJson(self):
        return {"id": self.id, "title": self.title, "content": self.content}


@app.post("/blog", status_code=201)
def create_blog_post(input: BlogCreationInputDTO, res: Response):
    logging.warning(f"Receiving request POST in /blog with body: {vars(input)}")
    try:
        blog_posts.append(BlogPost(input.id, input.title, input.content))
        logging.warning(f"Created blog: {vars(input)}")
        return {"status": "sucess"}
    except KeyError:
        logging.error(f"Failed to created blog: KeyError")
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Invalid request"}
    except Exception as e:
        logging.error(f"Failed to created blog: {e}")
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@app.get("/blog", status_code=200)
def get_blog_posts():
    logging.warning(f"Request to get all blogs received!")
    return {"posts": [blog.toJson() for blog in blog_posts]}


@app.get("/blog/{id}", status_code=200)
def get_blog_post(id: int, res: Response):
    logging.warning(f"Request to get blog with id: {id}, received!")
    for post in blog_posts:
        if post.id == id:
            return {"post": post.__dict__}
    logging.error(f"Unable to find blog post: {id}")
    res.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Post not found"}


@app.delete("/blog/{id}", status_code=200)
def delete_blog_post(id: int, res: Response):
    logging.warning(f"Request to delete posts in blog with id: {id} received!")
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            logging.warning(f"Post: {post} removed!")
            return {"status": "sucess"}
    logging.error(f"Post not found in blog: {id}!")
    res.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Post not found"}


@app.put("/blog/{id}", status_code=200)
def update_blog_post(id: int, input: BlogEditInputDTO, res: Response):
    logging.warning(
        f"Request to update blog post with id: {id} and body: {vars(input)} received!"
    )
    try:
        for post in blog_posts:
            if post.id == id:
                post.title = input.title
                post.content = input.content
                logging.warning(f"Post: {post} edited!")
                return {"status": "sucess"}

        logging.error(f"Post with id: {id} not found")
        res.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Post not found"}
    except KeyError:
        logging.error(f"Invalid request with id: {id} and body: {vars(input)}")
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Invalid request"}
    except Exception as e:
        logging.error(f"Error: {e}")
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
