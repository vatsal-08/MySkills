# Generated by Django 4.1.7 on 2023-06-03 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='joining_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_modified',
        ),
    ]