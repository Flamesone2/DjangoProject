# Generated by Django 5.1.3 on 2024-11-26 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ('id',), 'verbose_name': 'ToDo Item'},
        ),
    ]