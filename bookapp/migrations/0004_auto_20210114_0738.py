# Generated by Django 3.0 on 2021-01-14 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_auto_20210114_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='offer',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]