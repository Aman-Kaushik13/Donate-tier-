from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name="login"),
    path('donate/', views.donatePage, name="donate")
]
#urls for my web app
