# Generated by Django 2.2.6 on 2022-09-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0010_auto_20220913_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]