# Generated by Django 4.2.7 on 2023-11-17 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_applicanteducation_graduated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantcertificate',
            name='expired_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicantcertificate',
            name='received_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='company',
            name='revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='desired_degree',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='required_degree',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='vacancyapplication',
            name='hired_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
