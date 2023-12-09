from django.contrib import admin
from .models import Ingredient, Meal

# настраиваем админку
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'ingredients_amount']

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Meal, MealAdmin)