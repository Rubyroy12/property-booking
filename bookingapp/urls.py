from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('property/',views.property,name = 'property'),
    path('property/details/<name>/',views.details,name = 'details'),
    path('account/profile/<str:username>/',views.profile,name='profile'),
    path('booking/cart/<name>/',views.booking,name='booking'),
    path('property/order/',views.order,name='order'),
    path('delete/<int:id>',views.delete, name="delete"),
    path('search/$', views.search_results, name='search_results'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)