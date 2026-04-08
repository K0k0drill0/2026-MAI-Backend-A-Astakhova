from django.urls import path, include

urlpatterns = [
    path("web/", include("books.urls.web")),
    path("api/", include("books.urls.api")),
]
