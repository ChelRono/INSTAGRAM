# Generated by Django 4.0.5 on 2022-06-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(default=True),
        ),
    ]