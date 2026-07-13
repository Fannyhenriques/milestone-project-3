from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "recipe/<int:recipe_id>/",
        views.recipe_detail,
        name="recipe_detail",
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="mealflow/login.html"
        ),
        name="login",
    ),

    path("register/", 
         views.register_view, 
         name="register"
    ),


    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),
]