from django.contrib.gis.geoip2.resources import City
from django.shortcuts import render
from django import template
from .models import *
from django.contrib import messages
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.views.generic import ListView
from django.http import JsonResponse,HttpResponse
import json


def Home(request):
    return render(request, 'index.html')


def franchise_request(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        state=request.POST.get('state')
        district=request.POST.get('district')
        city=request.POST.get('city')
        message=f'Name: {name},' \
                f'Phone:{phone},' \
                f'Email:{email},' \
                f'State:{state},' \
                f'District:{district},' \
                f'City:{city}.'
        send_mail(
            'Franchise Request',
            message,
            'from@example.com',
            ['ajithkswork27@gmail.com'],
            fail_silently=False,
        )
        mail=franchise()
        mail.Name=name
        mail.Phone=phone
        mail.Email=email
        mail.State=state
        mail.District=district
        mail.City=city
        mail.save()
        return render(request, 'index.html')
    return render(request, 'index.html')


def search(request):
    if 'term' in request.GET:
        qs = Reg_Franchise.objects.filter(City__icontains=request.GET.get('term'))
        City = list()
        for product in qs:
            City.append(product.City)
        # titles = [product.title for product in qs]
        return JsonResponse(City, safe=False)
        return render(request, 'search.html')
    return render(request, 'search.html')

def search_result(request):
    return render(request,'search.html')









