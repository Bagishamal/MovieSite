# Generated by Django 3.2.9 on 2021-11-29 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='Movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Фильм'),
        ),
    ]