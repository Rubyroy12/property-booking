from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Property,Reviews
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

def details(request,name):
    # current_user= request.user
    home = Property.objects.get(name=name)
    # comment=Reviews.objects.filter(id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.property=property
            comment.user = request.user.profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form= ReviewsForm()
    params={
        'home':home,
        'form': form,
        # 'comment':comment,

        }
    return render(request,'details.html',params)




