# Generated by Django 4.0.3 on 2022-04-29 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wordofmouth', '0015_merge_0014_comment_0014_forkedrecipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forkedrecipe',
            old_name='originalRecipe',
            new_name='parent',
        ),
        migrations.AddField(
            model_name='forkedrecipe',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forkedrecipe',
            name='description',
            field=models.CharField(blank=True, max_length=175),
        ),
        migrations.AddField(
            model_name='forkedrecipe',
            name='directions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='forkedrecipe',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='forkedrecipe',
            name='title',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]