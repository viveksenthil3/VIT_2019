from django.urls import path
from .views import home, pdt_json, cart, register_from_mob, register_from_web, qr_generate, sms, drive, home_1, home_2, home_3
urlpatterns = [
    path('home/', home),
    path('pdts/', pdt_json),
    path('cart/', cart),
    path('register/', register_from_mob),
    path('checkout/', register_from_web),
    path('qr/', qr_generate),
    path('sms/', sms),
    path('drive/', drive),
    path('home1/', home_1),
    path('home2/', home_2),
    path('home3/', home_3)
]