# Generated by Django 4.0.4 on 2022-05-31 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_courses_added_alter_courses_last_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['-last_modified']},
        ),
    ]
