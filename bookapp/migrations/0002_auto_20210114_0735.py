# Generated by Django 3.0 on 2021-01-14 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
    ]
