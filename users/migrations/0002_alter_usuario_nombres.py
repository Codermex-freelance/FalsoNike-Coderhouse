# Generated by Django 4.0.4 on 2022-07-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre'),
        ),
    ]
