import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
import os

import pyqrcode
# import pypng
from django.conf import settings
import requests

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
    # print(request.POST.get('phone'))
    status = False
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

@csrf_exempt
def sms(request):
    if request.method == 'POST':
        if request.POST.get('pass') == 'pass':
            url = "https://www.fast2sms.com/dev/bulk"
            payload = "sender_id=FSTSMS&message={}&language=english&route=p&numbers=8667619406".format('come in')
            headers = {
                'authorization': "rNylIJvSoiB2QkFe3K8t1gDcPWxu4GfpCRzmZLwqM9X6H7UTbsaI2h0jX3uGnB9RQvr4o65NOmYUfWyZ",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            # response = requests.request("POST", url, data=payload, headers=headers)
            print(payload)


def drive(request):
    # g_login = GoogleAuth()
    # g_login.LocalWebserverAuth()
    # drive = GoogleDrive(g_login)
    #
    # with open(settings.BASE_DIR+'\static\QRCodes\8190031369.png', 'r') as file:
    #     file_drive = drive.CreateFile({'title':'8190031369.png'})
    #     file_drive.SetContentString(file.read())
    #     file_drive.Upload()
    return render(request, 'sms.html')


def home_1(request):
    return render(request, 'home1.html')


def home_2(request):
    return render(request, 'home2.html')


def home_3(request):
    return render(request, 'home3.html')