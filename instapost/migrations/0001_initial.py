# Generated by Django 4.1.1 on 2022-10-03 15:17
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ssum')),
            ],
        ),
        migrations.CreateModel(
            name='Instapost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
