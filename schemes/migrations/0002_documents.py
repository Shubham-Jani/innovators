# Generated by Django 4.1.1 on 2023-02-04 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=150)),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemes.scheme')),
            ],
            options={
                'db_table': 'documents',
                'unique_together': {('scheme', 'document')},
            },
        ),
    ]