# Generated by Django 3.2 on 2021-04-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.CharField(max_length=50)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
