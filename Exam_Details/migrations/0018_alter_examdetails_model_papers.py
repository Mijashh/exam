# Generated by Django 5.0.1 on 2024-01-31 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_Details', '0017_examdetails_model_papers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examdetails',
            name='model_papers',
            field=models.FileField(upload_to='static/Exam_Details/Model_Papers'),
        ),
    ]
