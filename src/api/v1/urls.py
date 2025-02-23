from django.urls import (path, include)

urlpatterns = [
    path(r'blog/', include('api.v1.blog.urls')),
    path(r'documents/', include('api.v1.documents.urls')),
]