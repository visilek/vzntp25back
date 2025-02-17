from django.urls import (path, include)

urlpatterns = [
    path(r'blog/', include('api.v1.blog.urls')),
    # path(r'blog/', include('blog.blog_images.api_urls')),
]