from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "recipe/<int:recipe_id>/",
        views.recipe_detail,
        name="recipe_detail",
    ),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("my-recipes/", views.my_recipes, name="my_recipes"),
]