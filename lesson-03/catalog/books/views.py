import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from books.models import Book, Category


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

def _serialize_book(b):
    return {
        "id": b.pk,
        "title": b.title,
        "author": b.author,
        "description": b.description,
        "cover": b.cover.url if b.cover else None,
        "published_at": b.published_at,
        "category_id": b.category.pk if b.category else None,
        "category": b.category.name if b.category else None,
        "created_at": b.created_at,
    }


@require_http_methods(["GET"])
def api_book_list(request):
    category_id = request.GET.get("category")
    qs = Book.objects.select_related("category").all()
    if category_id:
        qs = qs.filter(category_id=category_id)
    books = [_serialize_book(b) for b in qs]
    return JsonResponse({"books": books, "count": len(books)})

@require_http_methods(["POST"])
def api_book_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    title = data.get("title", "").strip()
    author = data.get("author", "").strip()
    if not title or not author:
        return JsonResponse({"error": "title and author are required"}, status=400)

    category = None
    category_id = data.get("category_id")
    if category_id is not None:
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return JsonResponse({"error": f"Category {category_id} not found"}, status=404)

    book = Book.objects.create(
        title=title,
        author=author,
        description=data.get("description", ""),
        published_at=data.get("published_at") or None,
        category=category,
    )
    return JsonResponse({"id": book.pk, "title": book.title, "author": book.author}, status=201)

@require_http_methods(["GET"])
def api_book_detail(request, book_id):
    return JsonResponse({"book_id": book_id, "title": "", "author": "", "category": ""})


@require_http_methods(["POST"])
def api_book_favorite(request, book_id):
    return JsonResponse({"book_id": book_id, "favorited": True})


@require_http_methods(["GET"])
def api_search(request):
    q = request.GET.get("q", "").strip()
    if not q:
        return JsonResponse({"error": "query param 'q' is required"}, status=400)

    qs = (
        Book.objects.select_related("category")
        .filter(title__icontains=q) | Book.objects.select_related("category").filter(description__icontains=q)
    ).distinct()

    books = [_serialize_book(b) for b in qs]
    return JsonResponse({"books": books, "count": len(books), "query": q})


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
