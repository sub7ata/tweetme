# Generated by Django 2.2.6 on 2019-10-26 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0010_auto_20191026_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='Liked',
            new_name='liked',
        ),
    ]
