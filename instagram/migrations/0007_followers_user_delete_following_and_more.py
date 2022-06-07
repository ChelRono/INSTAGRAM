# Generated by Django 4.0.5 on 2022-06-07 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_post_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pwd', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Following',
        ),
        migrations.AddField(
            model_name='followers',
            name='another_user',
            field=models.ManyToManyField(related_name='another_user', to='instagram.user'),
        ),
        migrations.AddField(
            model_name='followers',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='instagram.user'),
        ),
    ]
