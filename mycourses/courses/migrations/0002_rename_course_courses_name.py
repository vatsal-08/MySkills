# Generated by Django 4.0.4 on 2022-04-29 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='course',
            new_name='name',
        ),
    ]
