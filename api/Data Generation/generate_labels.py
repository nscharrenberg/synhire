import numpy as np
from faker import Faker

from api import models

Faker.seed(74321)
np.random.seed(74321)
fake = Faker()

industry_names = np.array(['Software Development', 'Hardware Manufacturing', 'Cybersecurity', 'Cloud Computing',
                           'Artificial Intelligence (AI) and Machine Learning',
                           'Data Analytics and Business Intelligence', 'Internet of Things (IoT)',
                           'Telecommunications',
                           'E-commerce and Online Retail', 'Digital Marketing and Advertising', 'Fintech',
                           'Healthcare IT', 'Gaming and Entertainment Technology', 'EdTech', 'Robotics',
                           'CleanTech',
                           'Big Data', 'Blockchain and Cryptocurrency', 'Mobile App Development',
                           'Cyber Forensics'])
industry_vacancies = np.array([['Senior Software Engineer', 'Frontend Developer', 'Quality Assurance Analyst'],
                               ['Hardware Design Engineer', 'Product Assembly Technician', 'Quality Control Inspector'],
                               ['Cybersecurity Analyst', 'Ethical Hacker', 'Information Security Manager'],
                               ['Cloud Solutions Architect', 'DevOps Engineer', 'Cloud Security Specialist'],
                               ['Machine Learning Engineer', 'AI Research Scientist', 'Data Scientist'],
                               ['Business Intelligence Analyst', 'Data Visualization Specialist', 'Big Data Engineer'],
                               ['IoT Solutions Architect', 'Embedded Systems Engineer', 'IoT Security Consultant'],
                               ['Network Engineer', 'Telecommunications Specialist', 'VoIP Engineer'],
                               ['E-commerce Manager', 'Online Marketing Specialist', 'Fulfillment Coordinator'],
                               ['Digital Marketing Manager', 'SEO Specialist', 'Social Media Strategist'],
                               ['Financial Analyst', 'Blockchain Developer', 'Payments Solutions Architect'],
                               ['Health IT Project Manager', 'Clinical Informatics Specialist',
                                'Telemedicine Specialist'],
                               ['Game Developer', 'UX/UI Designer for Gaming', '3D Animator'],
                               ['EdTech Product Manager', 'Online Learning Content Creator',
                                'Educational Software Developer'],
                               ['Robotics Engineer', 'Automation Specialist', 'Robotics Software Developer'],
                               ['Renewable Energy Engineer', 'Sustainability Analyst', 'Environmental Data Analyst'],
                               ['Big Data Architect', 'Data Engineer', 'Hadoop Administrator'],
                               ['Cryptocurrency Analyst', 'Smart Contract Developer',
                                'Blockchain Solutions Consultant'],
                               ['Mobile App Developer', 'iOS/Android Developer', 'Mobile App UI/UX Designer'],
                               ['Digital Forensics Investigator', 'Cybersecurity Forensics Analyst',
                                'Incident Response Specialist']
                               ])

languages = np.array(['English', 'Dutch', 'French', 'German'])


def generate_applicants(no_applicants):
    applicant_ids = np.array([i for i in range(no_applicants)])
    applicant_names = np.array([fake.name() for _ in range(no_applicants)])
    return applicant_ids, applicant_names


def generate_cerftificates(no_certificates):
    certificate_ids = np.array([i for i in range(no_certificates)])

    return certificate_ids

def generate_companies(no_companies):
    company_ids = np.array([i for i in range(no_companies)])
    company_names = np.array([fake.company() for _ in range(no_companies)])
    company_industries = np.array([industry_names[i] for i in np.random.randint(0, len(industry_names), no_companies)])
    company_size = np.random.randint(20, 1000, no_companies)
    company_revenue = np.array([i*np.randint(1000, 100000) for i in company_size])
    return company_ids, company_names, company_industries, company_size, company_revenue

def generate_institutes(no_institutes):
    institute_ids = np.array([i for i in range(no_institutes)])

    return institute_ids

#languages will be hardcoded

def generate_skills(no_skills):
    skill_ids = np.array([i for i in range(no_skills)])

    return skill_ids

print(generate_companies(5))
print(generate_applicants(5))
print(generate_institutes(5))

applicant_ids, applicant_names = generate_applicants(5)

for i in range(len(applicant_ids)):
    applicant = models.Applicant.objects.create(name=applicant_names[i], id=applicant_ids[i])
    applicant.save()

company_ids, company_names, company_industries = generate_companies(5)

for i in range(len(company_ids)):
    company = models.Company.objects.create(name=company_names[i], id=company_ids[i], industry=company_industries[i])
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