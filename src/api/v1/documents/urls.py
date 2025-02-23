from rest_framework.routers import DefaultRouter
from .document.views import DocumentViewset

router = DefaultRouter()
router.register(r"documents", DocumentViewset, basename="documents")
urlpatterns = router.urls
