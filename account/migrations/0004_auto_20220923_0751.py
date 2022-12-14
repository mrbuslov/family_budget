# Generated by Django 3.2.15 on 2022-09-23 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_family_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='member',
        ),
        migrations.AddField(
            model_name='account',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.family', verbose_name='Family'),
        ),
        migrations.AlterField(
            model_name='family',
            name='slug',
            field=models.SlugField(blank=True, default='b86f9b66e1e84df299feb426b9d78404', max_length=150, null=True, unique=True, verbose_name='Link'),
        ),
    ]
