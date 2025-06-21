from typing import List, Optional

from ..core.crud import CRUDBase
from ..models.content import Blog
from ..schemas.blogs import BlogCreate,BlogUpdate

from .category import category_controller

class BlogController(CRUDBase[Blog, BlogCreate, BlogUpdate]):
    def __init__(self):
        super().__init__(model=Blog)

    async def update_categories(self, blog: Blog, categories: List[int]) -> None:
        await blog.categories.clear()
        for category_id in categories:
            category_obj = await category_controller.get(id=category_id)
            await blog.categories.add(category_obj)

blog_controller = BlogController()
