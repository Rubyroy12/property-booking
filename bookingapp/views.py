from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import City, Property,Reviews,Cart
from django.contrib.auth.models import User
from .forms import ReviewsForm,BookingForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    myproperty=Property.objects.all()

    params = {
        'property':myproperty
    }
    return render(request, 'index.html',params)

@login_required(login_url='/accounts/login/')
def profile(request,username):
     

    return render(request,'profile.html')

def property(request):
    myproperty=Property.objects.all()

    params={
        'property':myproperty,
    }
    return render(request,'property.html',params)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def booking(request,name):
    appartment = Property.objects.get(name=name)
    myproperty= Property.objects.get(name=name)

    if request.method == 'POST':

        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user.profile
            book.property= myproperty
            book.save()
            message="Order made successfully"
            return HttpResponseRedirect(request.path_info,{'message':message})
    else:
        form = BookingForm()
    params={
        'appartment':appartment,
        'form':form,
        
    }
    return render(request,'cart.html',params)

def order(request):
    order= Cart.objects.all()
    params={
        'order':order,
    }
    return render(request,'order.html',params)

    
@login_required(login_url='/accounts/login/')
def delete(request,id):
    order= Cart.objects.get(id=id)
    order.delete()
    params={
        'order':order,
    }
  
    return render(request,'order.html' , params)

    
def search_results(request):

    if 'city' in request.GET and request.GET['city']:
        search_term = request.GET.get('city')
        searched_homes= Property.search_home(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"city":searched_homes})
    else:

        message = "You have not searched any city"

        return render(request,'search.html',{"message":message})
    
