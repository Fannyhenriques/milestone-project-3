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


