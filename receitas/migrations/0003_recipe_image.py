# Generated by Django 2.2.6 on 2022-07-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='foto_receita.png', upload_to='fotos/%Y/%m/%d/'),
        ),
    ]