# Generated by Django 3.2.15 on 2022-09-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family_budget', '0006_auto_20220923_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='slug',
            field=models.SlugField(blank=True, default='c63582b957184d389bbc994adf780f5c', max_length=150, null=True, unique=True, verbose_name='Link'),
        ),
    ]