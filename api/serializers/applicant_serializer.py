from rest_framework import serializers
from ..models import Applicant, ApplicantLanguage, ApplicantEducation, ApplicantSkill, ApplicantCertificate, \
    WorkExperience, Company, Language, EducationalInstitute, VacancySkill, VacancyLanguage, VacancyCertificate, Vacancy, \
    VacancyApplication


class ExEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = [
            'id',
            'name',
        ]


class CompanySerializer(serializers.ModelSerializer):
    ex_employees = ExEmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'size',
            'revenue',
            'industry',
            'rating',
            'description',
            'ex_employees'
        ]
        depth = 1


class ApplicantLanguageSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='language.name')

    class Meta:
        model = ApplicantLanguage
        fields = [
            'id',
            'name',
            'proficiency'
        ]


class ApplicantSkillSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='skill.name')

    class Meta:
        model = ApplicantSkill
        fields = [
            'id',
            'name',
            'proficiency'
        ]


class EducationalInstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitute
        fields = [
            'id',
            'name',
            'location'
        ]


class ApplicantEducationSerializer(serializers.ModelSerializer):
    institute = EducationalInstituteSerializer(many=False, read_only=True)

    class Meta:
        model = ApplicantEducation
        fields = [
            'id',
            'institute',
            'started_at',
            'graduated_at',
            'degree'
        ]


class ApplicantCertificateSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='certificate.name')

    class Meta:
        model = ApplicantCertificate
        fields = [
            'id',
            'name',
            'received_at',
            'expired_at'
        ]


class WorkExperienceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)

    class Meta:
        model = WorkExperience
        fields = [
            'id',
            'company',
            'hired_at',
            'left_at',
            'hired_reason',
            'left_reason',
            'role'
        ]


class VacancySkillSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='skill.name')

    class Meta:
        model = VacancySkill
        fields = [
            'id',
            'name',
            'desired_proficiency',
            'required_proficiency'
        ]


class VacancyLanguageSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='language.name')

    class Meta:
        model = VacancyLanguage
        fields = [
            'id',
            'name',
            'desired_proficiency',
            'required_proficiency'
        ]


class VacancyCertificateSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='certificate.name')

    class Meta:
        model = VacancyCertificate
        fields = [
            'id',
            'name',
            'required'
        ]


class VacancyForApplicantSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    certificates = VacancyCertificateSerializer(source='vacancycertificate_set', many=True)
    languages = VacancyLanguageSerializer(source='vacancylanguage_set', many=True)
    skills = VacancySkillSerializer(source='vacancyskill_set', many=True)

    class Meta:
        model = Vacancy
        fields = [
            'title',
            'role',
            'location',
            'salary',
            'desired_degree',
            'required_degree',
            'company',
            'certificates',
            'skills',
            'languages'
        ]


class ApplicantVacancySerializer(serializers.ModelSerializer):
    vacancy = VacancyForApplicantSerializer(many=False, read_only=True)

    class Meta:
        model = VacancyApplication
        fields = [
            'vacancy',
            'hired_at',
            'left_at',
            'hired_reason',
            'left_reason'
        ]


class ApplicantSerializer(serializers.ModelSerializer):
    languages = ApplicantLanguageSerializer(source='applicantlanguage_set', many=True)
    skills = ApplicantSkillSerializer(source='applicantskill_set', many=True)
    education = ApplicantEducationSerializer(source='applicanteducation_set', many=True)
    certificates = ApplicantCertificateSerializer(source='applicantcertificate_set', many=True)
    work_experience = WorkExperienceSerializer(source='workexperience_set', many=True)
    applications = ApplicantVacancySerializer(source='vacancyapplication_set', many=True)

    class Meta:
        model = Applicant
        fields = [
            'id',
            'name',
            'education',
            'certificates',
            'skills',
            'languages',
            'work_experience',
            'applications'
        ]
