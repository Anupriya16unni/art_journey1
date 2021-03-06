# Generated by Django 4.0.2 on 2022-05-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'artist_signup',
            },
        ),
    ]
