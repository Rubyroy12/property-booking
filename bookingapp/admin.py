from django.contrib import admin
from .models import Property,Gallery,City,Profile

# Register your models here.
admin.site.register(Property)
admin.site.register(Gallery)
admin.site.register(City)
admin.site.register(Profile)