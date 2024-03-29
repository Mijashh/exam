# Generated by Django 5.0.1 on 2024-01-30 08:36

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Details', '0008_alter_examindex_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examindex',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='exam_name', unique=True),
        ),
    ]
