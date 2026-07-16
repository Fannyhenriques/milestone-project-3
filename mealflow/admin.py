from django.contrib import admin

from .models import Category, Ingredient, Recipe, SavedRecipe


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 3


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "meal_type",
        "author",
        "created_at",
    )
    list_filter = ("category", "meal_type")
    search_fields = ("title", "description")
    inlines = [IngredientInline]


admin.site.register(Category)
admin.site.register(SavedRecipe)
