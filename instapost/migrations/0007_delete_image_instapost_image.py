# Generated by Django 4.1.1 on 2022-10-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapost', '0006_alter_image_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='instapost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]