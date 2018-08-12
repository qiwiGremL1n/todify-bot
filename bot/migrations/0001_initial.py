# Generated by Django 2.1 on 2018-08-11 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4096)),
                ('short_description', models.CharField(max_length=42)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_owner', to='bot.Person')),
            ],
        ),
    ]