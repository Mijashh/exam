# Generated by Django 5.0.1 on 2024-01-30 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Details', '0010_alter_examindex_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examindex',
            name='slug',
        ),
    ]
