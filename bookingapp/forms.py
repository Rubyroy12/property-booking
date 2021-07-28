from django import forms
from .models import Reviews,Cart
from django.contrib.auth.models import User



class ReviewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

    class Meta:
        model = Reviews
        fields = ('comment',)

class BookingForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields= ('card_No',)
        