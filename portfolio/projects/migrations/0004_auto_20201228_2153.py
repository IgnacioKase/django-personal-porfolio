# Generated by Django 2.2 on 2020-12-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_path',
            field=models.FileField(blank=True, default='default/default.jpg', null=True, upload_to='photo'),
        ),
    ]
