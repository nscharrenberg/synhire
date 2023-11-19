from api import models
from api.data_generation.generate_labels import generate_applicants, generate_companies, generate_institutes, \
    generate_skills, languages

applicant_ids, applicant_names = generate_applicants(5)

for i in range(len(applicant_ids)):
    applicant = models.Applicant.objects.create(name=applicant_names[i], id=applicant_ids[i])
    applicant.save()

company_ids, company_names, company_industries, company_size, company_revenue = generate_companies(5)

for i in range(len(company_ids)):
    company = models.Company.objects.create(name=company_names[i], id=company_ids[i], industry=company_industries[i],size=company_size, revenue=company_revenue)
    company.save()

institute_ids = generate_institutes(5)

for i in range(len(institute_ids)):
    institute = models.EducationalInstitute.objects.create(id=institute_ids[i])
    institute.save()

skill_ids = generate_skills(5)

for i in range(len(skill_ids)):
    skill = models.Skill.objects.create(id=skill_ids[i])
    skill.save()

for i in range(len(languages)):
    language = models.Language.objects.create(name=languages[i], id=i)
    language.save()
