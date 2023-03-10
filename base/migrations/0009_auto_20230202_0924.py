# Generated by Django 3.2.13 on 2023-02-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20230131_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentNo', models.CharField(max_length=200)),
                ('NAME', models.CharField(max_length=200)),
                ('ENGLISH', models.IntegerField(blank=True, null=True)),
                ('MATHEMATICS', models.IntegerField(blank=True, null=True)),
                ('ECONOMICS', models.IntegerField(blank=True, null=True)),
                ('GEOGRAPHY', models.IntegerField(blank=True, null=True)),
                ('GOVERNMENT', models.IntegerField(blank=True, null=True)),
                ('ANIMALHUSBANDRY', models.IntegerField(blank=True, null=True)),
                ('CIVICEDUCATION', models.IntegerField(blank=True, null=True)),
                ('ISLAMICSTUDIES', models.IntegerField(blank=True, null=True)),
                ('HAUSALANGUAGE', models.IntegerField(blank=True, null=True)),
                ('TOTAL', models.IntegerField(blank=True, null=True)),
                ('AVERAGE', models.FloatField(null=True)),
                ('POSITION', models.IntegerField(blank=True, null=True)),
                ('GENDER', models.CharField(max_length=20)),
                ('OUTOF', models.IntegerField(null=True)),
                ('CLASS', models.CharField(max_length=200)),
                ('TERM', models.CharField(max_length=20, null=True)),
                ('YEAR', models.CharField(max_length=20)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Junior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentNo', models.CharField(max_length=200)),
                ('NAME', models.CharField(max_length=200)),
                ('ENGLISH', models.IntegerField(blank=True, null=True)),
                ('MATHEMATICS', models.IntegerField(blank=True, null=True)),
                ('BASICSCIENCE', models.IntegerField(blank=True, null=True)),
                ('BASICTECHNOLOGY', models.IntegerField(blank=True, null=True)),
                ('PHE', models.IntegerField(blank=True, null=True)),
                ('AGRICULTURALSCIENCE', models.IntegerField(blank=True, null=True)),
                ('SOCIALSTUDIES', models.IntegerField(blank=True, null=True)),
                ('CIVICEDUCATION', models.IntegerField(blank=True, null=True)),
                ('ISLAMICSTUDIES', models.IntegerField(blank=True, null=True)),
                ('CCA', models.IntegerField(blank=True, null=True)),
                ('HAUSALANGUAGE', models.IntegerField(blank=True, null=True)),
                ('ARABICLANGUAGE', models.IntegerField(blank=True, null=True)),
                ('LITERATURE', models.IntegerField(blank=True, null=True)),
                ('BUSINESSSTUDIES', models.IntegerField(blank=True, null=True)),
                ('TOTAL', models.IntegerField(blank=True, null=True)),
                ('AVERAGE', models.FloatField(null=True)),
                ('POSITION', models.IntegerField(blank=True, null=True)),
                ('GENDER', models.CharField(max_length=20)),
                ('OUTOF', models.IntegerField(null=True)),
                ('CLASS', models.CharField(max_length=200)),
                ('TERM', models.CharField(max_length=20, null=True)),
                ('YEAR', models.CharField(max_length=20)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentNo', models.CharField(max_length=200)),
                ('NAME', models.CharField(max_length=200)),
                ('ENGLISH', models.IntegerField(blank=True, null=True)),
                ('MATHEMATICS', models.IntegerField(blank=True, null=True)),
                ('PHYSICS', models.IntegerField(blank=True, null=True)),
                ('CHEMISTRY', models.IntegerField(blank=True, null=True)),
                ('BIOLOGY', models.IntegerField(blank=True, null=True)),
                ('ANIMALHUSBANDRY', models.IntegerField(blank=True, null=True)),
                ('ISLAMICSTUDIES', models.IntegerField(blank=True, null=True)),
                ('GEOGRAPHY', models.IntegerField(blank=True, null=True)),
                ('ECONOMICS', models.IntegerField(blank=True, null=True)),
                ('GOVERNMENT', models.IntegerField(blank=True, null=True)),
                ('LITERATURE', models.IntegerField(blank=True, null=True)),
                ('HAUSALANGUAGE', models.IntegerField(blank=True, null=True)),
                ('TOTAL', models.IntegerField(blank=True, null=True)),
                ('AVERAGE', models.FloatField(null=True)),
                ('POSITION', models.IntegerField(blank=True, null=True)),
                ('GENDER', models.CharField(max_length=20)),
                ('OUTOF', models.IntegerField(null=True)),
                ('CLASS', models.CharField(max_length=200)),
                ('TERM', models.CharField(max_length=20, null=True)),
                ('YEAR', models.CharField(max_length=20)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='science',
            name='YEAR',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Qualification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
