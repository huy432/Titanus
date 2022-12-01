from django.urls import path
from useraccount.views import register, profile, verificationAccount, login
from django.contrib.auth import views as auth

urlpatterns = [
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('login/', login, name="login"),
    #path('login/',auth.LoginView.as_view(template_name='login/login.html'), name="login"),
    path('logout/',auth.LogoutView.as_view(next_page='/'),name='logout'),
    path('verification/<str:username>/<str:data>',verificationAccount , name="verification")
]