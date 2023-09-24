# Generated by Django 4.2.3 on 2023-08-31 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('qualification', models.TextField(max_length=50)),
                ('specialist', models.TextField(max_length=30)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
