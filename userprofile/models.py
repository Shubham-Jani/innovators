from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=True)
    # date_of_birth = models.DateField(datetime.datetime.now().date())
    age = models.IntegerField(default=18)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES,
                              default='male')
    #  single, married, widowed, divorced
    MARITAL_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('divorced', 'Divorced'),
    )
    marital_status = models.CharField(max_length=10,
                                      choices=MARITAL_CHOICES,
                                      default='Single')
    INCOME_CHOICES = (
        ('BPL', "Less Than 50000"),
        ('lower', "50000-250000"),
        ('middle', "250000-700000"),
        ('upper', 'Greater Than 700000'),
    )
    income_class = models.CharField(max_length=10,
                                    choices=INCOME_CHOICES,
                                    default='middle')

    # casts = SC ST OBC General

    CAST_CHOICES = (
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('general', 'General'),
    )
    cast_class = models.CharField(max_length=10,
                                  choices=CAST_CHOICES,
                                  default='general')

    EDUCATION_CHOICES = (
        ('primary', 'Primary education(till 8th class)'),
        ('secondary', 'Secondary education(till 10th class)'),
        ('senior_secondary', 'Senior Secondary education (till 12th class)'),
        ('undergraduate', ' Undergraduate education'),
        ('postgraduate', 'Postgraduate education'),
    )

    education_class = models.CharField(max_length=20,
                                       choices=EDUCATION_CHOICES,
                                       default='secondary')
