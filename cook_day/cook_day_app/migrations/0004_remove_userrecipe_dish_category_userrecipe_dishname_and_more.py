# Generated by Django 4.2.15 on 2024-08-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cook_day_app", "0003_userrecipe"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userrecipe",
            name="dish_category",
        ),
        migrations.AddField(
            model_name="userrecipe",
            name="dishname",
            field=models.TextField(default="Dosa"),
        ),
        migrations.RemoveField(
            model_name="userrecipe",
            name="ingredients",
        ),
        migrations.AlterField(
            model_name="userrecipe",
            name="instructions",
            field=models.TextField(default="mix well and cook on low flame"),
        ),
        migrations.AlterField(
            model_name="userrecipe",
            name="username",
            field=models.CharField(default="admin", max_length=255),
        ),
        migrations.AddField(
            model_name="userrecipe",
            name="ingredients",
            field=models.TextField(default="Rice batter, water, salt, curd"),
        ),
    ]
