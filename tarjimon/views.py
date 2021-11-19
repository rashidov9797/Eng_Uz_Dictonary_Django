from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugatlar

# Create your views here.


def index(request):
  soz = request.GET.get('q','')
  if soz and soz != '':
    natija = Lugatlar.objects.filter(english__contains=soz).all()[:3]
  else:
    natija = None  


  return render(request,'index.html',{'q':soz,'natija':natija})