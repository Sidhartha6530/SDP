from django.urls import path
from .views import *

urlpatterns=[
    path('',merlin,name="m2"),
    path('login.html',login,name="l"),
    path('registration',register,name="r"),
    path('categories.html',categories,name="c"),
    path('contact.html',contact,name="co"),
    path('merlin.html',merlin,name="m"),
    path('products.html',products,name="p"),
    path('index.html',index,name="i2")

]