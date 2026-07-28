from django.urls import path 
from . import views
app_name = 'users'
urlpatterns = [
    path('register/',views.RegisterUser, name='RegisterUser'),
    path('login/',views.LoginUser, name='LoginUser'),
    path('logout/',views.LogoutUser, name='LogoutUser')
]
