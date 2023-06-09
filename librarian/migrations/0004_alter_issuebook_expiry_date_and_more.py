# Generated by Django 4.0.6 on 2022-08-23 07:59

from django.db import migrations, models
import librarian.models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='expiry_date',
            field=models.DateTimeField(default=librarian.models.get_expiry),
        ),
        migrations.AlterField(
            model_name='issuebook',
            name='issue_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
