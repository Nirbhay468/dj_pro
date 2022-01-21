
from django.urls import path
from .views import News, Home, Contact, NewsDate, NewsP, register, addUser

urlpatterns = [
    path('', Home, name = 'home'), 
    path('news/', NewsP, name = 'news'),
    path('contact/', Contact, name = 'contact'),
    path('newsdate/<int:year>',NewsDate, name='newsdate'),
    path('signup/', register, name = 'register'),
     path('adduser/', addUser, name = 'addUser')
 

]