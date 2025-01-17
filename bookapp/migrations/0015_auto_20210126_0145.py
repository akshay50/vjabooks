# Generated by Django 3.0 on 2021-01-26 01:45

from django.db import migrations, models
import storages.backends.sftpstorage


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0014_auto_20210124_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverphoto',
            field=models.ImageField(storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='coverphoto/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='indexsample',
            field=models.FileField(blank=True, storage=storages.backends.sftpstorage.SFTPStorage(), upload_to='bookindex/'),
        ),
    ]
