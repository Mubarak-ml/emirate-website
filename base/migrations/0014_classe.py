# Generated by Django 3.2.13 on 2023-02-20 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20230218_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('master', models.CharField(blank=True, max_length=200, null=True)),
                ('detail', models.TextField(blank=True, null=True)),
                ('snumber', models.IntegerField(blank=True, null=True)),
                ('pict', models.ImageField(blank=True, default='course-5.jpeg', null=True, upload_to='')),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
