# Generated by Django 2.2.6 on 2022-09-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_auto_20220901_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>/fotos/%d/%m/%Y'),
        ),
    ]