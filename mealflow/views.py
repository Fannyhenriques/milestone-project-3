from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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


def my_recipes(request):
    return render(request, "mealflow/my_recipes.html")