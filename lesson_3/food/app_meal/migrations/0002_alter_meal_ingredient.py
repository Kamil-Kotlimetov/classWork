# Generated by Django 4.0 on 2023-12-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_meal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='ingredient',
            field=models.ManyToManyField(related_name='meals', to='app_meal.Ingredient', verbose_name='ингредиенты'),
        ),
    ]