from django.shortcuts import render
from .models import Category, Dish


def main_page_view(request):

    categories = Category.objects.filter(is_visible=True)
    return render(request, 'main_page.html', context={
        'categories': categories
    })