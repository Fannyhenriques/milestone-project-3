from .forms import RecipeForm
from .models import Ingredient, Recipe, SavedRecipe
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

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


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "mealflow/register.html",
        context,
    )


@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            ingredient_lines = (
                form.cleaned_data["ingredients"].splitlines()
            )

            for order, line in enumerate(
                ingredient_lines,
                start=1,
            ):
                ingredient_name = line.strip()

                if ingredient_name:
                    Ingredient.objects.create(
                        recipe=recipe,
                        name=ingredient_name,
                        quantity="",
                        order=order,
                    )

            return redirect(
                "recipe_detail",
                recipe_id=recipe.id,
            )
    else:
        form = RecipeForm()

    context = {
        "form": form,
        "page_title": "Create recipe",
        "button_text": "Create recipe",
    }

    return render(
        request,
        "mealflow/recipe_form.html",
        context,
    )


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        author=request.user,
    )

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            recipe = form.save()

            recipe.ingredients.all().delete()

            ingredient_lines = (
                form.cleaned_data["ingredients"].splitlines()
            )

            for order, line in enumerate(
                ingredient_lines,
                start=1,
            ):
                ingredient_name = line.strip()

                if ingredient_name:
                    Ingredient.objects.create(
                        recipe=recipe,
                        name=ingredient_name,
                        quantity="",
                        order=order,
                    )

            return redirect(
                "recipe_detail",
                recipe_id=recipe.id,
            )
    else:
        existing_ingredients = "\n".join(
            ingredient.name
            for ingredient in recipe.ingredients.all()
        )

        form = RecipeForm(
            instance=recipe,
            initial={
                "ingredients": existing_ingredients,
            },
        )

    context = {
        "form": form,
        "recipe": recipe,
        "page_title": "Edit recipe",
        "button_text": "Save changes",
    }

    return render(
        request,
        "mealflow/recipe_form.html",
        context,
    )


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
        author=request.user,
    )

    if request.method == "POST":
        recipe.delete()
        return redirect("my_recipes")

    return redirect(
        "recipe_detail",
        recipe_id=recipe.id,
    )


def my_recipes(request):
    return render(request, "mealflow/my_recipes.html")