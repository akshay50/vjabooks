# Generated by Django 3.0 on 2021-01-16 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0009_book_launchdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='launchdate',
        ),
        migrations.AddField(
            model_name='book',
            name='comingsoon',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='book',
            name='onboard_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
