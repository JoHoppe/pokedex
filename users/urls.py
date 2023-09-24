from django.urls import path

from users import views


app_name = 'users'

urlpatterns = [
    path("login", views.custom_login, name="login"),
    path("register", views.custom_register, name="register"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("logout", views.CustomLogoutView.as_view(), name="logout"),
    path("search_profile",views.searchProfile,name="search_Profile")


]
