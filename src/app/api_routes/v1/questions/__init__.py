from fastapi import APIRouter
from .get import router as get_router
from .post import router as post_router
from .delete import router as delete_router

router = APIRouter()

# Include all question routes
router.include_router(get_router, tags=["questions"])
router.include_router(post_router, tags=["questions"])
router.include_router(delete_router, tags=["questions"])
