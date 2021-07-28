from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)

class City(models.Model):
    name = models.CharField(max_length = 50)

class Property(models.Model):
    city = models.ForeignKey(City,on_delete = models.CASCADE,related_name = 'property')
    name= models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.CharField(max_length=500)
    rooms=models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)

class Gallery(models.Model):
    property= models.ForeignKey(Property, on_delete = models.CASCADE, related_name = 'gallery')
    image1 = CloudinaryField('image')
    image2 = CloudinaryField('image')
    image3= CloudinaryField('image')

class Reviews(models.Model):
    comment = models.TextField()
    user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='comment')
    property = models.ForeignKey('Property',on_delete=models.CASCADE,related_name='comment')

    class Meta:
        ordering = ["-pk"]
    
    def __str__(self):
        return f'{self.user.name} Property'

# class Paymentmode(models.Model):
#     mode= models.CharField(max_length=100,blank=True)

class Cart(models.Model):
    user= models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='booking')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    card_No= models.CharField(max_length=100)
    

