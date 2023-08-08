from django.urls import path

from users import views


app_name = 'users'

urlpatterns = [
    path("login", views.custom_login, name="login"),
    path("register", views.custom_register, name="register"),
    path("my_profile", views.my_profile, name="my_profile"),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),

]
