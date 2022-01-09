from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_home,name='home'),
    path('',views.password_que,name='password_que'),
    path('', views.index, name='vote'),
]