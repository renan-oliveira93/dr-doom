# Generated by Django 5.0.4 on 2024-04-16 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_rename_title_image_image_title'),
        ('post', '0002_post_published_post_subtitle_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_image', to='image.image'),
        ),
    ]