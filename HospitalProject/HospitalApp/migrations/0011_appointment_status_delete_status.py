# Generated by Django 4.2.3 on 2023-09-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0010_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.TextField(max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]