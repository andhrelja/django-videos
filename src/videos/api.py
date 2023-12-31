from django.http import JsonResponse
from .models import (
    CATEGORY_TYPE_CHOICES,
    CATEGORY_SUBTYPE_CHOICES
)

def get_categories(request):
    category_names = dict(CATEGORY_TYPE_CHOICES)
    category_classes = dict(CATEGORY_SUBTYPE_CHOICES).values()
    return JsonResponse({
        "0": dict(
            name=category_names['ELEMENTARY'],
            classes=list(category_classes)
        ),
        "1": dict(
            name=category_names['HIGH'],
            classes=list(category_classes)[:4]
        )
    })