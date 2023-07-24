from django.shortcuts import render, get_object_or_404
from .models import Dish, Category

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'dish/dish_list.html', {'dishes': dishes})

def dish_detail(request, slug):
    dish = get_object_or_404(Dish, slug=slug)
    context = {
        'dish': dish,
        'menu_hero_image': 'path/to/menu_hero.jpg',  # Replace with the actual path to your menu_hero image
    }
    return render(request, 'dish_detail.html', context)
  

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def home_view(request):
    dishes = Dish.objects.all()
    return render(request, 'home.html', {'dishes':dishes})

def menu(request):
    dishes =  Dish.objects.all()
    return render(request, 'menu.html', {'dishes':dishes})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')