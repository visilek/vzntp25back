from rest_framework.routers import DefaultRouter
from .blogpost.views import BlogpostViewset
from .blog_rubric.views import BlogRubricViewset
from .blogpost_tag.views import BlogpostTagViewset

router = DefaultRouter()
router.register(r"blog-rubrics", BlogRubricViewset, basename="blog-rubrics")
router.register(r"blogposts", BlogpostViewset, basename="blogposts")
router.register(r"blogposts-tags", BlogpostTagViewset, basename="blogpost-tags")
urlpatterns = router.urls
