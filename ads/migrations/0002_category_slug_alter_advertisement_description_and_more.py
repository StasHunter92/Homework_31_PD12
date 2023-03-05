# Generated by Django 4.1.7 on 2023-03-03 17:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=50, null=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='name',
            field=models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
