from django.contrib import admin

from .models import Category, Ingredient, Dish

# admin.site.register(Category)
# admin.site.register(Ingredient)
# admin.site.register(Dish)

# Define an inline formset for the ingredients field
class DishIngredientsInline(admin.TabularInline):
    model = Dish.ingredients.through
    extra = 1  # Number of empty ingredient forms to display by default

# Register the models and customize the Dish admin to include the inline formset
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = [DishIngredientsInline]  # Include the inline formset for ingredients

    # Customize the display fields in the change list view
    list_display = ['name', 'category']

    # Optionally, customize the filter options for the change list view
    list_filter = ['category']

    # Optionally, customize the search field for the change list view
    search_fields = ['name']
