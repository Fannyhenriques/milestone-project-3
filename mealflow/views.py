from django.shortcuts import get_object_or_404, render

from .models import Recipe


def home(request):
    recipes = Recipe.objects.all()

    context = {
        "recipes": recipes,
    }

    return render(request, "mealflow/home.html", context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    context = {
        "recipe": recipe,
    }

    return render(request, "mealflow/recipe_detail.html", context)


