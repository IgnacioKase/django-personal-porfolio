# Generated by Django 2.2 on 2020-12-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20201229_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='is_menu_item',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_path',
            field=models.FileField(blank=True, default='default/default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image_path',
            field=models.FileField(blank=True, default='default/icons.jpg', null=True, upload_to=''),
        ),
    ]
