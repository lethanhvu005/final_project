from django.urls import path 
from . import views
app_name = 'users'
urlpatterns = [
    path('register/',views.RegisterUser, name='RegisterUser'),
    path('login/',views.LoginUser, name='LoginUser'),
    path('logout/',views.LogoutUser, name='LogoutUser'),
    path('account/',views.Account,name='Account'),
    path('forgot_password/',views.forgot_password, name='Forgot_password'),
    path('change_password/<uidb64>/<token>/',views.change_password, name ='change_password')
]
