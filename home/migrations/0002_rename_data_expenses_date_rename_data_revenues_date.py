# Generated by Django 5.1.1 on 2024-09-13 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='revenues',
            old_name='data',
            new_name='date',
        ),
    ]
