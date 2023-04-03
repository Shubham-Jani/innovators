# Generated by Django 4.1.1 on 2022-10-11 18:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='demo scheme', max_length=300, unique=True)),
                ('scheme_info', models.TextField(default='empty', max_length=500)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced'), ('any', 'any')], default='any', max_length=10)),
                ('age', models.CharField(choices=[('0-18', '0-18'), ('18-50', '18-50'), ('50-125', '50-125'), ('any', 'any')], default='any', max_length=30)),
                ('link', models.URLField(default='www.google.com')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('last_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'scheme',
            },
        ),
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.CharField(choices=[('BPL', 'Less Than 50000'), ('lower', '50000-250000'), ('middle', '250000-700000'), ('upper', 'Greater Than 700000'), ('any', 'any')], max_length=30)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemes.scheme')),
            ],
            options={
                'db_table': 'incomes',
                'unique_together': {('scheme', 'income')},
            },
        ),
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other'), ('any', 'any')], max_length=30)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemes.scheme')),
            ],
            options={
                'db_table': 'genders',
                'unique_together': {('scheme', 'gender')},
            },
        ),
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(choices=[('primary', 'Primary education(till 8th class)'), ('secondary', 'Secondary education(till 10th class)'), ('senior_secondary', 'Senior Secondary education (till 12th class)'), ('undergraduate', ' Undergraduate education'), ('postgraduate', 'Postgraduate education'), ('any', 'any')], max_length=30)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemes.scheme')),
            ],
            options={
                'db_table': 'educations',
                'unique_together': {('scheme', 'education')},
            },
        ),
        migrations.CreateModel(
            name='Catagories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(choices=[('education', 'education'), ('startup', 'startup'), ('agriculture', 'agriculture'), ('other', 'other')], max_length=30)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemes.scheme')),
            ],
            options={
                'db_table': 'catagories',
                'unique_together': {('scheme', 'catagory')},
            },
        ),
        migrations.CreateModel(
            name='Castes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caste', models.CharField(choices=[('general', 'general'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('any', 'any')], max_length=30)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemes.scheme')),
            ],
            options={
                'db_table': 'castes',
                'unique_together': {('scheme', 'caste')},
            },
        ),
    ]