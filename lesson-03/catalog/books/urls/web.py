from django.urls import path
from books import views

urlpatterns = [
    path("",                            views.web_index,       name="web-index"),
    path("category/<int:category_id>/", views.web_category,    name="web-category"),
    path("books/<int:book_id>/",        views.web_book_detail, name="web-book-detail"),
    path("profile/",                    views.web_profile,     name="web-profile"),
]
