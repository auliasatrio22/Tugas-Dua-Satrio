# Generated by Django 4.1.1 on 2022-10-13 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
    ]
