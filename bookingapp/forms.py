from django import forms
from .models import Reviews
from django.contrib.auth.models import User



class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields= ('comment',)
        