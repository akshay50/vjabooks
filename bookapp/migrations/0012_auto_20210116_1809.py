# Generated by Django 3.0 on 2021-01-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0011_auto_20210116_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='buylinkcod',
            field=models.URLField(blank=True),
        ),
    ]
