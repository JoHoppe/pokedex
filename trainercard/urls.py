from django.urls import path

from users import views


app_name = 'trainercard'

urlpatterns = [
    path("login", views.custom_login, name="login"),
    path("register", views.custom_register, name="register"),
    path("profile", views.profile, name="profile"),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),


]
