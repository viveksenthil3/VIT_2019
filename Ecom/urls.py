from django.urls import path
from .views import home, pdt_json, cart
urlpatterns = [
    path('home/', home),
    path('pdts/', pdt_json),
    path('cart/', cart),
]