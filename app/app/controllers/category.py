from typing import List, Optional

from ..core.crud import CRUDBase
from ..models.content import Category
from ..schemas.categories import CategoryCreate,CategoryUpdate

class CategoryController(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def __init__(self):
        super().__init__(model=Category)

    async def get_category_ids(self)->List[int]:
        return [category.id for category in await self.model.all()]
category_controller = CategoryController()
