# Generated by Django 4.2.1 on 2023-05-27 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_articulo_creador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='creador',
            new_name='user',
        ),
    ]
