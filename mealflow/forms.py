from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "maxlength": 100,
                "placeholder": "Enter a recipe title.",
            }
        ),
    )

    ingredients = forms.CharField(
        label="Ingredients",
        help_text="Enter one ingredient per line.",
        widget=forms.Textarea(
            attrs={
                "rows": 8,
                "placeholder": (
                    "Enter one ingredient per line.\n"
                    "Example:\n"
                    "2 garlic cloves\n"
                    "250 ml cream"
                ),
            }
        ),
    )

    class Meta:
        model = Recipe
        fields = [
            "category",
            "title",
            "description",
            "ingredients",
            "instructions",
            "meal_type",
            "servings",
            "cooking_time",
        ]