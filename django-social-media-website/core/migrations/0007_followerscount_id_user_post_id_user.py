# Generated by Django 4.2.dev20221102162115 on 2022-12-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='followerscount',
            name='id_user',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='id_user',
            field=models.IntegerField(default=0),
        ),
    ]
