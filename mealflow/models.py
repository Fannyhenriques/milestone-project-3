from django.conf import settings
from django.db import models


class Category(models.Model):
    """
    Represents a food category and its default recipe image.
    """

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    default_image = models.CharField(
        max_length=200,
        help_text=(
            "Static image path, for example: "
            "mealflow/images/recipes/default-fish.jpg"
        ),
    )

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Represents a recipe created by a registered user.
    """

    MEAL_TYPE_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("dessert", "Dessert"),
    ]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="recipes",
    )
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True)
    instructions = models.TextField()
    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_TYPE_CHOICES,
    )
    servings = models.PositiveIntegerField(default=4)
    cooking_time = models.PositiveIntegerField(
        help_text="Total cooking time in minutes.",
    )
    image_name = models.CharField(
        max_length=150,
        blank=True,
        help_text=(
            "Optional static image filename for built-in recipes. "
            "Leave blank to use the category image."
        ),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def image_path(self):
        """
        Returns the recipe's own static image when available,
        otherwise the category's default image.
        """
        if self.image_name:
            return f"mealflow/images/recipes/{self.image_name}"

        return self.category.default_image


class Ingredient(models.Model):
    """
    Represents one ingredient belonging to a recipe.
    """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )
    quantity = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        if self.quantity:
            return f"{self.quantity} {self.name}"

        return self.name
    

