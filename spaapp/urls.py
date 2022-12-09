from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('membership', views.membership, name='membership'),
    path('owner', views.owner, name='owner')
]
