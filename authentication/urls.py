from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signUp', views.signUp, name="signUp"),
    path('signIn', views.signIn, name="signIn"),
    path('signOut', views.signOut, name="signOut"),
    path('loanProvider', views.loanProvider, name="loanProvider"),
    path('loanCustomer', views.loanCustomer, name="loanCustomer"),
    path('bankPersonnel', views.bankPersonnel, name="bankPersonnel"),
    path('createdLoans', views.createdLoans, name="createdLoans"),
]
