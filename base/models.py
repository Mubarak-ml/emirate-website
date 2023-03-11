from django.db import models

# Create your models here.
TCHOICES = (
    ('2022/2023','2022/2023'),
    ('2023/2024', '2023/2024'),
    ('2024/2025','2024/2025'),
    ('2025/2026','2025/2026'),
)

GCHOICES = (
    ('MALE','MALE'),
    ('FEMALE', 'FEMALE'),   
)

YCHOICES = (
    ('FIRST','FIRST'),
    ('SECOND', 'SECOND'),
    ('THIRD', 'THIRD'),    
)




class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    fpict = models.ImageField(null=True, blank=True)
    spict = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    pict = models.ImageField(null=True, blank=True, default="avatar.jpeg")
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Classe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    master = models.CharField(max_length=200, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    snumber = models.IntegerField(null=True, blank=True)
    pict = models.ImageField(null=True, blank=True, default="course-5.jpeg")
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#STUDENTS RESULTS MODELS

class Science(models.Model):
    StudentNo = models.CharField(max_length=200)
    NAME = models.CharField(max_length=200)
    ENGLISH = models.IntegerField(null=True, blank=True)
    MATHEMATICS = models.IntegerField(null=True, blank=True)
    PHYSICS = models.IntegerField(null=True, blank=True)
    CHEMISTRY = models.IntegerField(null=True, blank=True)
    BIOLOGY = models.IntegerField(null=True, blank=True)
    ANIMALHUSBANDRY = models.IntegerField(null=True, blank=True)
    CIVICEDUCATION = models.IntegerField(null=True, blank=True)
    ISLAMICSTUDIES = models.IntegerField(null=True, blank=True)
    HAUSALANGUAGE = models.IntegerField(null=True, blank=True)
    TOTAL = models.IntegerField(null=True, blank=True)
    AVERAGE = models.FloatField(null=True)
    POSITION = models.IntegerField(null=True, blank=True)
    GENDER = models.CharField(max_length=20, choices=GCHOICES)
    OUTOF = models.IntegerField(null=True)
    CLASS = models.CharField(max_length=200)
    TERM = models.CharField(max_length=20, null=True, choices=YCHOICES)
    YEAR = models.CharField(max_length=20, null=False, blank=False, choices=TCHOICES)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NAME

class Arts(models.Model):
    StudentNo = models.CharField(max_length=200)
    NAME = models.CharField(max_length=200)
    ENGLISH = models.IntegerField(null=True, blank=True)
    MATHEMATICS = models.IntegerField(null=True, blank=True)
    ECONOMICS = models.IntegerField(null=True, blank=True)
    GEOGRAPHY = models.IntegerField(null=True, blank=True)
    GOVERNMENT = models.IntegerField(null=True, blank=True)
    ANIMALHUSBANDRY = models.IntegerField(null=True, blank=True)
    CIVICEDUCATION = models.IntegerField(null=True, blank=True)
    ISLAMICSTUDIES = models.IntegerField(null=True, blank=True)
    HAUSALANGUAGE = models.IntegerField(null=True, blank=True)
    TOTAL = models.IntegerField(null=True, blank=True)
    AVERAGE = models.FloatField(null=True)
    POSITION = models.IntegerField(null=True, blank=True)
    GENDER = models.CharField(max_length=20, choices=GCHOICES)
    OUTOF = models.IntegerField(null=True)
    CLASS = models.CharField(max_length=200)
    TERM = models.CharField(max_length=20, null=True, choices=YCHOICES)
    YEAR = models.CharField(max_length=20, null=False, blank=False, choices=TCHOICES)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NAME

class Sone(models.Model):
    StudentNo = models.CharField(max_length=200)
    NAME = models.CharField(max_length=200)
    ENGLISH = models.IntegerField(null=True, blank=True)
    MATHEMATICS = models.IntegerField(null=True, blank=True)
    PHYSICS = models.IntegerField(null=True, blank=True)
    CHEMISTRY = models.IntegerField(null=True, blank=True)
    BIOLOGY = models.IntegerField(null=True, blank=True)
    ANIMALHUSBANDRY = models.IntegerField(null=True, blank=True)
    ISLAMICSTUDIES = models.IntegerField(null=True, blank=True)
    GEOGRAPHY = models.IntegerField(null=True, blank=True)
    ECONOMICS = models.IntegerField(null=True, blank=True)
    GOVERNMENT = models.IntegerField(null=True, blank=True)
    LITERATURE = models.IntegerField(null=True, blank=True)
    HAUSALANGUAGE = models.IntegerField(null=True, blank=True)
    TOTAL = models.IntegerField(null=True, blank=True)
    AVERAGE = models.FloatField(null=True)
    POSITION = models.IntegerField(null=True, blank=True)
    GENDER = models.CharField(max_length=20, choices=GCHOICES)
    OUTOF = models.IntegerField(null=True)
    CLASS = models.CharField(max_length=200)
    TERM = models.CharField(max_length=20, null=True, choices=YCHOICES)
    YEAR = models.CharField(max_length=20, null=False, blank=False, choices=TCHOICES)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NAME


class Junior(models.Model):
    StudentNo = models.CharField(max_length=200)
    NAME = models.CharField(max_length=200)
    ENGLISH = models.IntegerField(null=True, blank=True)
    MATHEMATICS = models.IntegerField(null=True, blank=True)
    BASICSCIENCE = models.IntegerField(null=True, blank=True)
    BASICTECHNOLOGY = models.IntegerField(null=True, blank=True)
    PHE = models.IntegerField(null=True, blank=True)
    AGRICULTURALSCIENCE = models.IntegerField(null=True, blank=True)
    SOCIALSTUDIES = models.IntegerField(null=True, blank=True)
    CIVICEDUCATION = models.IntegerField(null=True, blank=True)
    ISLAMICSTUDIES = models.IntegerField(null=True, blank=True)
    CCA = models.IntegerField(null=True, blank=True)
    HAUSALANGUAGE = models.IntegerField(null=True, blank=True)
    ARABICLANGUAGE = models.IntegerField(null=True, blank=True)
    LITERATURE = models.IntegerField(null=True, blank=True)
    BUSINESSSTUDIES = models.IntegerField(null=True, blank=True)
    TOTAL = models.IntegerField(null=True, blank=True)
    AVERAGE = models.FloatField(null=True)
    POSITION = models.IntegerField(null=True, blank=True)
    GENDER = models.CharField(max_length=20, choices=GCHOICES)
    OUTOF = models.IntegerField(null=True)
    CLASS = models.CharField(max_length=200)
    TERM = models.CharField(max_length=20, null=True, choices=YCHOICES)
    YEAR = models.CharField(max_length=20, null=False, blank=False, choices=TCHOICES)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NAME