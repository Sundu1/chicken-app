# Generated by Django 4.1.7 on 2023-03-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='CreatedAt',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='ModifiedAt',
            field=models.DateTimeField(),
        ),
    ]
