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
        "recipe/<int:recipe_id>/save/",
        views.toggle_save_recipe,
        name="toggle_save_recipe",
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

    path("my-recipes/", 
         views.my_recipes, 
         name="my_recipes"
    ),

    path(
        "create-recipe/",
        views.create_recipe,
        name="create_recipe",
    ),

    path(
        "recipe/<int:recipe_id>/edit/",
        views.edit_recipe,
        name="edit_recipe",
    ),

    path(
        "recipe/<int:recipe_id>/delete/",
        views.delete_recipe,
        name="delete_recipe",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="home"),
        name="logout",
    ),
]