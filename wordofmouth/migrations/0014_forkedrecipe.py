# Generated by Django 4.0.2 on 2022-04-18 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordofmouth', '0013_remove_recipe_favorites_alter_favoriterecipe_recipe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForkedRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='staticfiles/recipe.png', upload_to='staticfiles')),
                ('originalRecipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordofmouth.recipe')),
            ],
        ),
    ]
