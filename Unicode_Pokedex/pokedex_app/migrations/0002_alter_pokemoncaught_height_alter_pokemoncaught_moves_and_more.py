# Generated by Django 4.2 on 2023-09-10 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncaught',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pokemoncaught',
            name='moves',
            field=models.JSONField(default='No moves'),
        ),
        migrations.AlterField(
            model_name='pokemoncaught',
            name='sprites',
            field=models.JSONField(default='No sprites'),
        ),
    ]
