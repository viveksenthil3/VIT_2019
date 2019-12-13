from django.urls import path
from .views import home, pdt_json, cart, register_from_mob, register_from_web, qr_generate
urlpatterns = [
    path('home/', home),
    path('pdts/', pdt_json),
    path('cart/', cart),
    path('register/', register_from_mob),
    path('checkout/', register_from_web),
    path('qr/', qr_generate)
]