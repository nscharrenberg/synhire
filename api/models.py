from enum import Enum

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class EducationalInstitute(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Language(models.Model):
    name = models.CharField(max_length=255, unique=True)
    applicants = models.ManyToManyField(to='Applicant', through='ApplicantLanguage')
    vacancies = models.ManyToManyField(to='Vacancy', through='VacancyLanguage')

    def __str__(self):
        return f"{self.name}"


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    applicants = models.ManyToManyField(to='Applicant', through='ApplicantSkill')
    vacancies = models.ManyToManyField(to='Vacancy', through='VacancySkill')

    def __str__(self):
        return f"{self.name}"


class Certificate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    applicants = models.ManyToManyField(to='Applicant', through='ApplicantCertificate')
    vacancies = models.ManyToManyField(to='Vacancy', through='VacancyCertificate')

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(validators=[MinValueValidator(0)])
    revenue = models.DecimalField(null=True, blank=True, max_digits=18, decimal_places=2, validators=[MinValueValidator(0.00)])
    industry = models.CharField(max_length=255)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField(null=True, blank=True)
    ex_employees = models.ManyToManyField(to='Applicant', through='WorkExperience')

    def __str__(self):
        return f"{self.name} ({self.industry} - {self.size})"


class Applicant(models.Model):
    name = models.CharField(max_length=200)
    languages = models.ManyToManyField(to='Language', through='ApplicantLanguage')
    education = models.ManyToManyField(to='EducationalInstitute', through='ApplicantEducation')
    skills = models.ManyToManyField(to='Skill', through='ApplicantSkill')
    external_experience = models.ManyToManyField(to='Company', through='WorkExperience')
    certificates = models.ManyToManyField(to='Certificate', through='ApplicantCertificate')
    vacancies = models.ManyToManyField(to='Vacancy', through='VacancyApplication')

    def __str__(self):
        return f"{self.name}"


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    desired_degree = models.TextField(null=True, blank=True)
    required_degree = models.TextField(null=True, blank=True)
    role = models.TextField()
    skills = models.ManyToManyField(to='Skill', through='VacancySkill')
    languages = models.ManyToManyField(to='Language', through='VacancyLanguage')
    certificates = models.ManyToManyField(to='Certificate', through='VacancyCertificate')
    applications = models.ManyToManyField(to='Applicant', through='VacancyApplication')

    def __str__(self):
        return f"{self.title} ({self.company}|{self.location}|{self.role}|{self.salary})"


class ApplicantLanguage(models.Model):
    applicant = models.ForeignKey(to='Applicant', on_delete=models.CASCADE)
    language = models.ForeignKey(to='Language', on_delete=models.CASCADE)
    proficiency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class ApplicantEducation(models.Model):
    applicant = models.ForeignKey(to='Applicant', on_delete=models.CASCADE)
    institute = models.ForeignKey(to='EducationalInstitute', on_delete=models.CASCADE)
    started_at = models.DateField()
    graduated_at = models.DateField(null=True, blank=True)
    degree = models.TextField()

    def __str__(self):
        return f"{self.applicant} studied {self.degree} at {self.institute}"


class ApplicantSkill(models.Model):
    applicant = models.ForeignKey(to='Applicant', on_delete=models.CASCADE)
    skill = models.ForeignKey(to='Skill', on_delete=models.CASCADE)
    proficiency = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.applicant} masters {self.skill}"


class ApplicantCertificate(models.Model):
    applicant = models.ForeignKey(to='Applicant', on_delete=models.CASCADE)
    certificate = models.ForeignKey(to='Certificate', on_delete=models.CASCADE)
    received_at = models.DateField(null=True, blank=True)
    expired_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.applicant} received {self.certificate}"


class WorkExperience(models.Model):
    applicant = models.ForeignKey(to='Applicant', on_delete=models.CASCADE)
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE)
    hired_at = models.DateField()
    left_at = models.DateField(null=True, blank=True)
    hired_reason = models.TextField(null=True, blank=True)
    left_reason = models.TextField(null=True, blank=True)
    role = models.TextField()

    def __str__(self):
        return f"{self.applicant} worked as a {self.role} at {self.company}"


class VacancySkill(models.Model):
    vacancy = models.ForeignKey(to='Vacancy', on_delete=models.CASCADE)
    skill = models.ForeignKey(to='Skill', on_delete=models.CASCADE)
    desired_proficiency = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    required_proficiency = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.vacancy} expects the applicant to have the skill: {self.skill}"


class VacancyLanguage(models.Model):
    vacancy = models.ForeignKey(to='Vacancy', on_delete=models.CASCADE)
    language = models.ForeignKey(to='Language', on_delete=models.CASCADE)
    desired_proficiency = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    required_proficiency = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.vacancy} expects the applicant to have the language: {self.language}"


class VacancyCertificate(models.Model):
    vacancy = models.ForeignKey(to='Vacancy', on_delete=models.CASCADE)
    certificate = models.ForeignKey(to='Certificate', on_delete=models.CASCADE)
    required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vacancy} expects the applicant to have certificate: {self.certificate}"


class VacancyApplication(models.Model):
    vacancy = models.ForeignKey(to='Vacancy', on_delete=models.CASCADE)
    applicant = models.ForeignKey(to='Applicant', on_delete=models.CASCADE)
    hired_at = models.DateField(null=True, blank=True)
    left_at = models.DateField(null=True, blank=True)
    hired_reason = models.TextField(null=True, blank=True)
    left_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.applicant} applied to {self.vacancy}"
