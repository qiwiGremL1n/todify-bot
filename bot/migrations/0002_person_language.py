# Generated by Django 2.1 on 2018-08-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='language',
            field=models.CharField(default='RU', max_length=8),
            preserve_default=False,
        ),
    ]
