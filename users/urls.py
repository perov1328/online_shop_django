from django.urls import path
from users.apps import UsersConfig
from users.views.fbv import generate_new_password, verify
from users.views.cbv import LoginView, LogoutView, RegisterView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('verify/', verify, name='verification'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
]