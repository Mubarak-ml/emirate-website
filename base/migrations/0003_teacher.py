# Generated by Django 3.2.13 on 2023-01-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_news_pict'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('Qualification', models.CharField(max_length=200)),
                ('pict', models.ImageField(blank=True, null=True, upload_to='')),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
