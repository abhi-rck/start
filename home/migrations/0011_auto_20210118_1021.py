# Generated by Django 3.1.5 on 2021-01-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210118_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingpeerlearning',
            name='img',
            field=models.ImageField(upload_to='upcomingsession/'),
        ),
    ]
