# Generated by Django 4.1.2 on 2023-01-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitravel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdatas',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
