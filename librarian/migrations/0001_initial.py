# Generated by Django 4.0.6 on 2022-07-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddNewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('isbn', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('subject_area', models.CharField(max_length=255)),
            ],
        ),
    ]
