# Generated by Django 3.2.6 on 2022-06-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_userprofile_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='_a',
            field=models.CharField(default='Qrlrp5wWpMhGgqUy', max_length=16),
        ),
    ]
