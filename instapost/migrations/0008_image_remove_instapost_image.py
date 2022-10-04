# Generated by Django 4.1.1 on 2022-10-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapost', '0007_delete_image_instapost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='instapost',
            name='image',
        ),
    ]