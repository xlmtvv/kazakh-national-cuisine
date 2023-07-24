from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cuisine'

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
            # Генерируем slug из названия блюда перед сохранением
            if not self.slug:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name