from django.urls import path
from . import views

 # name used to uniquely indentify this URL. Can be used to reverse mapper. For example link pages to home using <a href="{% url 'index' %}">Home</a>
urlpatterns = [
    path('', views.index, name='index'),
]
