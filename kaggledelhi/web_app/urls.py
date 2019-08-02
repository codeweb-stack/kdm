from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('speakers/',views.speakers,name='speakers'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('free-tickets/',views.free_tickets,name='free-tickets')
    
]