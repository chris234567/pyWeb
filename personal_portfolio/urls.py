from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("About/", include("About.urls")),
]
