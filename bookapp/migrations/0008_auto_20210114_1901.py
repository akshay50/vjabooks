# Generated by Django 3.0 on 2021-01-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0007_auto_20210114_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='offer',
            field=models.PositiveIntegerField(blank=True, default='1'),
        ),
    ]
