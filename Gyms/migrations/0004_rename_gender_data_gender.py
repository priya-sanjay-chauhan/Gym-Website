# Generated by Django 4.1.5 on 2023-03-26 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gyms', '0003_data_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='gender',
            new_name='Gender',
        ),
    ]