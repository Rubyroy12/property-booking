from django import forms
from .models import Reviews,Cart
from django.contrib.auth.models import User



class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields= ('comment',)
class BookingForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields= ('card_No',)
        