import tornado

from blog.models import Blog
from handlers import BaseHandler
from utils import Routers


@Routers("/")
class BlogList(BaseHandler):
    async def get(self, *args, **kwargs):
        blogs = await Blog.find({})
        self.write(blogs)

    async def post(self, *args, **kwargs):
        data = tornado.escape.json_decode(self.request.body)
        blog = Blog(**data)
        inserted_id = await blog.commit()
        self.write("%s" % inserted_id)
