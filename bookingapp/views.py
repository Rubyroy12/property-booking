from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Property,Reviews,Profile
from django.contrib.auth.models import User
from .forms import ReviewsForm


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

def property(request):
    myproperty=Property.objects.all()

    params={
        'property':myproperty,
    }
    return render(request,'property.html',params)


def details(request,name):
    home = Property.objects.get(name=name)
   
    comment= Reviews.objects.all()
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.property = home
            comment.user = request.user.profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ReviewsForm()
    params={
        'home': home,
        'form': form,
        'comments':comment,
        

        }
    return render(request,'details.html',params)




