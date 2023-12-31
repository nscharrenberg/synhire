# Generated by Django 4.2.7 on 2023-11-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vacancy_language_applicants_workexperience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='vacancies',
            field=models.ManyToManyField(through='api.VacancyApplication', to='api.vacancy'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
