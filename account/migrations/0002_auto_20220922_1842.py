# Generated by Django 3.2.15 on 2022-09-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='owner',
        ),
        migrations.AddField(
            model_name='account',
            name='member',
            field=models.ManyToManyField(blank=True, null=True, to='account.Family', verbose_name='Family'),
        ),
        migrations.AlterField(
            model_name='family',
            name='slug',
            field=models.SlugField(blank=True, default='ac88907b27c74e309fd973bcf5cd8d82', max_length=150, null=True, unique=True, verbose_name='Link'),
        ),
    ]