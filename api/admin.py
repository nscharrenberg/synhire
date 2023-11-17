from django.contrib import admin

from api.models import Applicant, Company, Skill, Language, Certificate, Vacancy, EducationalInstitute


class ApplicantSkillInline(admin.TabularInline):
    model = Applicant.skills.through
    extra = 0


class ApplicantLanguageInline(admin.TabularInline):
    model = Applicant.languages.through
    extra = 0


class ApplicantCertificateInline(admin.TabularInline):
    model = Applicant.certificates.through
    extra = 0


class ApplicantEducationInline(admin.TabularInline):
    model = Applicant.education.through
    extra = 0


class ApplicantWorkExperienceInline(admin.TabularInline):
    model = Applicant.external_experience.through
    extra = 0


class VacancyApplicantInline(admin.TabularInline):
    model = Vacancy.applications.through
    extra = 0


@admin.register(Applicant)
class ApplicantModel(admin.ModelAdmin):
    inlines = [
        ApplicantWorkExperienceInline,
        ApplicantEducationInline,
        ApplicantSkillInline,
        ApplicantLanguageInline,
        ApplicantCertificateInline,
        VacancyApplicantInline
    ]


class VacancySkillInline(admin.TabularInline):
    model = Vacancy.skills.through
    extra = 0


class VacancyLanguageInline(admin.TabularInline):
    model = Vacancy.languages.through
    extra = 0


class VacancyCertificateInline(admin.TabularInline):
    model = Vacancy.certificates.through
    extra = 0


@admin.register(Vacancy)
class VacancyModel(admin.ModelAdmin):
    inlines = [
        VacancySkillInline,
        VacancyLanguageInline,
        VacancyCertificateInline,
        VacancyApplicantInline
    ]


@admin.register(EducationalInstitute)
class EducationalInstituteModel(admin.ModelAdmin):
    inlines = [
        ApplicantEducationInline
    ]


admin.site.register(Company)
admin.site.register(Skill)
admin.site.register(Language)
admin.site.register(Certificate)
