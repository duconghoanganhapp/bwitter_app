# Generated by Django 4.2.dev20221102162115 on 2022-12-18 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_post_id_user_post_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followerscount',
            name='id_user',
        ),
        migrations.AddField(
            model_name='followerscount',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
            preserve_default=False,
        ),
    ]
