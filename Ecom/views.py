import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

import pyqrcode
# import pypng
from django.conf import settings

from .forms import CustomerRegisterationForm
from .models import customer_data
from VIT_2019 import settings

def home(request):
    # print(settings.STATIC_ROOT)
    dic = {
        'imgs': [
            'static/img/slider/img01.jpg',
            'static/img/slider/img02.jpg',
            'static/img/slider/img03.jpg',
            'static/img/slider/img04.jpg'
        ]
    }
    return render(request, 'index.html', dic)

@csrf_exempt
def pdt_json(request):
    print("in")
    if request.method == 'POST':
        res = None

        #To identify the request format and parse accordingly
        if request.headers['Content-Type'] == "application/x-www-form-urlencoded":
            j = urllib.parse.parse_qs(request.body.decode('utf-8'))
            res = j['pdts'][0]

        # elif request.headers['Content-Type'] == "application/json":
        #     j = json.loads(request.body)
        #     res = j['pdts']

        if res == '?':
            print("got you")
            dic = {
                'pdts': [
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
                ],
                'imgs': [
                    'static/img/slider/img01.jpg',
                    'static/img/slider/img02.jpg',
                    'static/img/slider/img03.jpg',
                    'static/img/slider/img04.jpg'
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


@csrf_exempt
def register_from_mob(request):
    if request.method == 'POST':
        res = None

        # To identify the request format and parse accordingly
        # if request.headers['Content-Type'] == "application/x-www-form-urlencoded":
            # j = urllib.parse.parse_qs(request.body.decode('utf-8'))

        # print(request.POST.get('name'))
        status = 0
        query = customer_data.objects.filter(phone='+91' + request.POST.get('phone'))
        if len(query) == 0:
            status = 1
            cus_db = customer_data(name=request.POST.get('name'), phone=request.POST.get('phone'), location=request.POST.get('location'))
            cus_db.save()


        # j['name'][0] += ' Success'
        js = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'location': request.POST.get('location'),
            'status': status
        }
        # js= {'status': status,
        #      'name': request.POST.get('name')}

        return JsonResponse(js)


def register_from_web(request):
    form = CustomerRegisterationForm(request.POST or None)
    print(request.POST.get('phone'))

    if form.is_valid():
        status = 0
        query = customer_data.objects.filter(phone='+91'+request.POST.get('phone'))
        if len(query) == 0:
            status =1
            form.save()
            form = CustomerRegisterationForm()

    return render(request, 'checkout.html', {'form':form , 'status': status})

@csrf_exempt
def qr_generate(request):
    if request.method == 'POST':
        url = pyqrcode.create(request.POST.get('phone'))
        path = settings.BASE_DIR + "\static\QRCodes\\"
        no = request.POST.get('phone')
        url.png(path+no+".png", scale=8)
        return JsonResponse({'qrUrl': '/static/QRCodes/'+no+'.png'})
        # print()