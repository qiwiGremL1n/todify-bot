# Generated by Django 2.1 on 2018-08-12 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_person_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='df', max_length=42),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='short_description',
            field=models.CharField(max_length=126),
        ),
    ]
