# Generated by Django 2.2.26 on 2022-05-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220521_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userId',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
