# Generated by Django 3.2.13 on 2022-06-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iwriter', '0003_alter_postrequests_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postrequests',
            name='post_request',
            field=models.IntegerField(default=0),
        ),
    ]
