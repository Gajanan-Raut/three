from django.contrib import admin
from django.urls import path
from threeapp import views

urlpatterns = [
    path('home',views.home),
    path('about',views.about),
    path('create',views.create),
    path('delete/<n>',views.delete),
    # path('edit/<n>',views.edit),
    path('dashboard',views.dashboard),
    path('all',views.dashboard),
    path('htol',views.htol),
    path('ltoh',views.ltoh),
    path('dform',views.showform),
    path('forms',views.show),
    path('stu',views.stu),
    path('modelform',views.showmodelform),
    path('cview',views.MyView.as_view()),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('set',views.setcookie),
    path('get',views.getcookie),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('delsession',views.del_session),
    path('getid',views.getloggeduserid)
    

]
