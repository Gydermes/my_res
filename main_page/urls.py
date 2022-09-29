from django.urls import path, include
from .views import main_page_view

aoo_name = 'main_page'

urlpatterns = [
    path('', main_page_view)
]