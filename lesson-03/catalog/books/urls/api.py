from django.urls import path
from books import views

urlpatterns = [
    path("books/",                          views.api_book_list,     name="api-book-list"),
    path("books/<int:book_id>/",            views.api_book_detail,   name="api-book-detail"),
    path("books/<int:book_id>/favorite/",   views.api_book_favorite, name="api-book-favorite"),
    path("categories/",                     views.api_category_list, name="api-category-list"),
    path("profile/",                        views.api_profile,       name="api-profile"),
    path("auth/register/",                  views.api_auth_register, name="api-auth-register"),
    path("auth/login/",                     views.api_auth_login,    name="api-auth-login"),
    path("auth/logout/",                    views.api_auth_logout,   name="api-auth-logout"),
]
