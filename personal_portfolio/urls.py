from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("About/", include("About.urls")),
]
