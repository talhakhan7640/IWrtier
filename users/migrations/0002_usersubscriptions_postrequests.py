# Generated by Django 3.2.13 on 2022-06-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscriptions',
            name='postRequests',
            field=models.IntegerField(default=0),
        ),
    ]
