from django.urls import path
from .views import home, pdt_json
urlpatterns = [
    path('home/', home),
    path('pdts/', pdt_json),
]