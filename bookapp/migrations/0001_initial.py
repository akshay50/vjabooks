# Generated by Django 3.0 on 2021-01-14 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toweight', models.PositiveIntegerField()),
                ('length', models.PositiveIntegerField(blank=True)),
                ('breadth', models.PositiveIntegerField(blank=True)),
                ('height', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('markedprice', models.PositiveIntegerField(default='1')),
                ('sellingprice', models.PositiveIntegerField(default='1')),
                ('indexsample', models.FileField(upload_to='bookindex/')),
                ('pages', models.PositiveSmallIntegerField()),
                ('coverphoto', models.ImageField(upload_to='coverphoto/')),
                ('seller', models.CharField(choices=[("Brainy Bro's Online Services", "Brainy Bro's Online Services")], default='1', max_length=100)),
                ('delivery', models.CharField(choices=[('3-5 Days', '3-5 Days')], default='1', max_length=100)),
                ('offer', models.CharField(default='1', max_length=100)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('buylink', models.URLField(default='1')),
                ('stock', models.BooleanField(default=False)),
                ('author', models.ManyToManyField(to='bookapp.Author')),
                ('categories', models.ManyToManyField(to='bookapp.Category')),
                ('competitionexam', models.ManyToManyField(to='bookapp.CompetitionExam')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.Publisher')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.Weight')),
            ],
        ),
    ]