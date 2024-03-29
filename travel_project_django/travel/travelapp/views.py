from django.shortcuts import render
from .models import Place,Team

# Create your views here.
def index(request):
    data=Place.objects.all()

    team=Team.objects.all()

    return render(request,'index.html',{'data':data,'team':team})