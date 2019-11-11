from django.urls import path
from .import views
app_name='candlelight'
urlpatterns =[
    path('',views.index,name='home'),
    path('login/',views.web,name='login'),
    path('logout/', views.myy, name='logout'),
    path('register/',views.regg,name='register')
]