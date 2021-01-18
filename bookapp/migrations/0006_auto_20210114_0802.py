# Generated by Django 3.0 on 2021-01-14 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_auto_20210114_0739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='buylink',
            new_name='buylinkcod',
        ),
        migrations.RemoveField(
            model_name='book',
            name='weight',
        ),
        migrations.AddField(
            model_name='book',
            name='buylinkonline',
            field=models.URLField(default='1'),
        ),
        migrations.AddField(
            model_name='book',
            name='codcharge',
            field=models.PositiveIntegerField(default='1'),
        ),
    ]
