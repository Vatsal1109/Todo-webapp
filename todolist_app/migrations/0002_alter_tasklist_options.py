# Generated by Django 3.2.7 on 2021-09-05 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
