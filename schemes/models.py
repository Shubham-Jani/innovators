from email.policy import default
from random import choices
from django.db import models
import datetime
from datetime import date

# Create your models here.


class Scheme(models.Model):
    name = models.CharField(max_length=300, default="demo scheme", unique=True)
    scheme_info = models.TextField(max_length=500, default="empty")
    MARITAL_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),
        ('any', 'any'),
    )
    marital_status = models.CharField(max_length=10,
                                      choices=MARITAL_CHOICES,
                                      default="any")
    AGE_CHOICES = (
        ('0-18', '0-18'),
        ('18-50', '18-50'),
        ('50-125', '50-125'),
        ('any', 'any')
    )
    age = models.CharField(default='any', choices=AGE_CHOICES, max_length=30)
    link = models.URLField(default="www.google.com")
    start_date = models.DateField(default=datetime.date.today)
    last_date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'scheme'

    def __str__(self):
        return self.name

    @property
    def is_past_due(self):
        return date.today() > self.last_date


class Genders(models.Model):
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
        ('any', 'any')
    )
    gender = models.CharField(
        max_length=30, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'genders'
        unique_together = (('scheme', 'gender'))

    def __str__(self):
        return (self.scheme.name + " --> " + self.gender)


class Incomes(models.Model):
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE)
    INCOME_CHOICES = (
        ('BPL', "Less Than 50000"),
        ('lower', "50000-250000"),
        ('middle', "250000-700000"),
        ('upper', 'Greater Than 700000'),
        ('any', 'any'),
    )
    # max_income_class = models.CharField(max_length=10,
    #                                     choices=INCOME_CHOICES,
    #                                     default="any")
    income = models.CharField(
        max_length=30, choices=INCOME_CHOICES)

    class Meta:
        db_table = 'incomes'
        unique_together = (('scheme', 'income'))


class Educations(models.Model):
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE)
    EDUCATION_CHOICES = (
        ('primary', 'Primary education(till 8th class)'),
        ('secondary', 'Secondary education(till 10th class)'),
        ('senior_secondary', 'Senior Secondary education (till 12th class)'),
        ('undergraduate', ' Undergraduate education'),
        ('postgraduate', 'Postgraduate education'),
        ('any', 'any'),
    )
    education = models.CharField(
        max_length=30, choices=EDUCATION_CHOICES)

    class Meta:
        db_table = 'educations'
        unique_together = (('scheme', 'education'))


class Castes(models.Model):
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE)
    CASTE_CHOICES = (
        ('general', 'general'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('any', 'any'),
    )
    caste = models.CharField(
        max_length=30, choices=CASTE_CHOICES)

    class Meta:
        db_table = 'castes'
        unique_together = (('scheme', 'caste'))


class Catagories(models.Model):
    scheme = models.ForeignKey(
        Scheme, on_delete=models.CASCADE)
    CATAGORY_CHOICES = (
        ('education', 'education'),
        ('startup', 'startup'),
        ('agriculture', 'agriculture'),
        ("other", "other"),
    )
    catagory = models.CharField(
        max_length=30, choices=CATAGORY_CHOICES)

    class Meta:
        db_table = 'catagories'
        unique_together = (('scheme', 'catagory'))


class Documents(models.Model):
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    DOCUMENT_CHOICES = (
        ('adhar_card', 'Adhar Card'),
        ('income_certificate', 'Income Certificate'),
        ('cast_certificate', 'Cast Certificate'),
        ('SSC_marksheet', 'SSC Marksheet'),
        ('leaving_certificate', 'Leaving Certificate'),
        ('PAN_card', 'PAN Card'),
        ('reservation_certificate', 'Reservation Certificate'),
        ('driving_licence', 'Driving Licence'),
        ('passport', 'Passport')
    )
    document = models.CharField(max_length=150, choices=DOCUMENT_CHOICES)

    class Meta:
        db_table = 'documents'
        unique_together = (('scheme', 'document'))
