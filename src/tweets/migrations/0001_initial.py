# Generated by Django 2.2.6 on 2019-10-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TimeField()),
                ('content2', models.TimeField()),
                ('content3', models.TimeField()),
            ],
        ),
    ]
