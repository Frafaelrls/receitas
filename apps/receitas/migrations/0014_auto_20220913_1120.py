# Generated by Django 2.2.6 on 2022-09-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0013_auto_20220913_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]