# Generated by Django 4.0.5 on 2022-06-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
    ]