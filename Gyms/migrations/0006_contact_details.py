# Generated by Django 4.1.5 on 2023-03-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gyms', '0005_alter_data_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=60)),
                ('Email', models.CharField(max_length=70)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
