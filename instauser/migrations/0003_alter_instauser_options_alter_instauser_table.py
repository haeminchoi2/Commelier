# Generated by Django 4.1.1 on 2022-09-30 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instauser', '0002_alter_instauser_is_dating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instauser',
            options={},
        ),
        migrations.AlterModelTable(
            name='instauser',
            table='member',
        ),
    ]