from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# Web-views (/web/*)  — в будущем будут возвращать HTML

@require_http_methods(["GET"])
def web_index(request):
    """Главная страница — лента всех книг."""
    return JsonResponse({"page": "index", "description": "Лента всех книг"})


@require_http_methods(["GET"])
def web_category(request, category_id):
    return JsonResponse({"page": "category", "category_id": category_id})


@require_http_methods(["GET"])
def web_book_detail(request, book_id):
    return JsonResponse({"page": "book_detail", "book_id": book_id})


@require_http_methods(["GET"])
def web_profile(request):
    return JsonResponse({"page": "profile", "description": "Личный кабинет"})


# API-views (/api/*)  — возвращают JSON

@require_http_methods(["GET"])
def api_book_list(request):
    category_id = request.GET.get("category")
    return JsonResponse({
        "books": [],
        "filter": {"category_id": category_id},
    })


@require_http_methods(["GET"])
def api_book_detail(request, book_id):
    return JsonResponse({"book_id": book_id, "title": "", "author": "", "category": ""})


@require_http_methods(["POST"])
def api_book_favorite(request, book_id):
    return JsonResponse({"book_id": book_id, "favorited": True})


@require_http_methods(["GET"])
def api_category_list(request):
    return JsonResponse({"categories": []})


@require_http_methods(["GET"])
def api_profile(request):
    return JsonResponse({"user": None, "favorites": []})


@require_http_methods(["POST"])
def api_auth_register(request):
    return JsonResponse({"status": "registered", "user": None})


@require_http_methods(["POST"])
def api_auth_login(request):
    return JsonResponse({"status": "logged_in", "token": ""})


@require_http_methods(["POST"])
def api_auth_logout(request):
    return JsonResponse({"status": "logged_out"})
