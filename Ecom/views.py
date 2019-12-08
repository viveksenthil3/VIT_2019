import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from VIT_2019 import settings

def home(request):
    # print(settings.STATIC_ROOT)
    return render(request, 'index.html')

@csrf_exempt
def pdt_json(request):
    print("in")
    if request.method == 'POST':
        print(request.body)
        j = json.loads(request.body)
        print(j['pdts'])
        if j['pdts']=='?':
            print("got you")
            dic = {
                'pdts':[
                    {
                        'imgURL': 'static/img/mobile.jpeg',
                        'pdt-title': 'Mobile',
                        'pdt-content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam nemo placeat ratione repudiandae.',
                        'price': '12000'
                    },
                    {
                        'imgURL': 'static/img/beds.jpeg',
                        'pdt-title': 'Beds',
                        'pdt-content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam nemo placeat ratione repudiandae.',
                        'price': '25000'
                    },
                    {
                        'imgURL': 'static/img/women.jpeg',
                        'pdt-title': "Women's fashion",
                        'pdt-content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam nemo placeat ratione repudiandae.',
                        'price': '1500'
                    },
                    {
                        'imgURL': 'static/img/men.jpeg',
                        'pdt-title': "Men's fashion",
                        'pdt-content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam nemo placeat ratione repudiandae.',
                        'price': '1250'
                    }
                ]
            }

            return JsonResponse(dic)
        
        
def cart(request):
    if request.method == 'GET':
        imgURL = request.GET.get('imgURL');
        title =  request.GET.get('title');
        content = request.GET.get('content');
        price = request.GET.get('price');

        context = {
            'imgURL': imgURL,
            'title': title,
            'content': content,
            'price': price
        }
        return render(request, 'cart.html', context)
