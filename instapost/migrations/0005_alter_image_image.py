# Generated by Django 4.1.1 on 2022-10-04 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapost', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
