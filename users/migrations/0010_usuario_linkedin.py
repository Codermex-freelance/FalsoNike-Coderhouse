# Generated by Django 4.0.4 on 2022-07-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_usuario_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin'),
        ),
    ]
