from django import forms
from .models import User,Property,Reviews
from django.db.migrations.operations import fields

class ReviewsForm(forms.Form):
    class Meta:
        model=Reviews
        fields= ('comment')
        