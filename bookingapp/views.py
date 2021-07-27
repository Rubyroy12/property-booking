from django.shortcuts import render
from .models import Property
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    myproperty=Property.objects.all()

    params = {
        'property':myproperty
    }
    return render(request, 'index.html',params)


def profile(request,username):
    current_user = request.user

    return render(request,'profile.html')

def details(request,name):
    home = Property.objects.get(name=name)
    




