import random
import numpy as np
from faker import Faker
from django.utils import timezone

from api.models import (EducationalInstitute, Language, Skill, Certificate, Company,
                        Applicant, Vacancy, ApplicantLanguage, ApplicantSkill,
                        ApplicantCertificate, WorkExperience, ApplicantEducation,
                        VacancySkill, VacancyLanguage, VacancyCertificate, VacancyApplication)

# Set seed for reproducibility
np.random.seed(42)

fake = Faker()

# Define a correlation matrix for skills
correlation_matrix = np.array([[1.0, 0.7, 0.3],
                               [0.7, 1.0, 0.5],
                               [0.3, 0.5, 1.0]])


def generate_synthetic_educational_institutes(num_institutes):
    return [EducationalInstitute.objects.create(name=fake.company(), location=fake.city()) for _ in
            range(num_institutes)]


def generate_synthetic_languages(num_languages):
    return [Language.objects.create(name=fake.word()) for _ in range(num_languages)]


def generate_synthetic_skills(num_skills):
    return [Skill.objects.create(name=fake.word()) for _ in range(num_skills)]


def generate_synthetic_certificates(num_certificates):
    return [Certificate.objects.create(name=fake.word()) for _ in range(num_certificates)]


def generate_synthetic_companies(num_companies):
    return [Company.objects.create(
        name=fake.company(),
        size=np.random.randint(1, 1000),
        revenue=np.random.uniform(100000, 100000000),
        industry=fake.word(),
        rating=np.random.uniform(1, 5),
        description=fake.text()
    ) for _ in range(num_companies)]


def generate_synthetic_applicants(num_applicants, institutes, languages, skills, certificates, companies):
    applicants = []

    for _ in range(num_applicants):
        # Generate random applicant name
        name = fake.name()

        # Randomly choose an educational institute
        institute = np.random.choice(institutes)

        # Generate random education details
        started_at = fake.date_of_birth(minimum_age=20, maximum_age=30)
        graduated_at = fake.date_of_birth(minimum_age=25, maximum_age=35) if np.random.choice([True, False]) else None
        degree = fake.text()

        # Generate random language proficiencies
        language_proficiencies = {
            language: max(1, int(np.random.normal(3, 1)))
            for language in languages
        }

        # Generate random certificates
        certificates_list = certificates[:np.random.randint(0, len(certificates))]

        # Generate random work experience
        work_experience = []
        for _ in range(np.random.randint(1, 4)):
            company = np.random.choice(companies)
            hired_at = fake.date_of_birth(minimum_age=20, maximum_age=30)
            left_at = fake.date_of_birth(minimum_age=25, maximum_age=35) if np.random.choice([True, False]) else None
            hired_reason = fake.text()
            left_reason = fake.text()
            role = fake.text()

            work_experience.append({
                "company": company,
                "hired_at": hired_at,
                "left_at": left_at,
                "hired_reason": hired_reason,
                "left_reason": left_reason,
                "role": role,
            })

        # Create an Applicant object
        applicant = Applicant.objects.create(name=name)

        # Create ApplicantEducation object
        ApplicantEducation.objects.create(
            applicant=applicant,
            institute=institute,
            started_at=started_at,
            graduated_at=graduated_at,
            degree=degree
        )

        # Create ApplicantLanguage objects
        for language, proficiency in language_proficiencies.items():
            ApplicantLanguage.objects.create(
                applicant=applicant,
                language=language,
                proficiency=proficiency
            )

        # Create ApplicantSkill objects with correlated proficiency levels
        skill_values = np.random.multivariate_normal([4, 4, 4], correlation_matrix, size=1)
        for index, skill in enumerate(skills):
            if len(skill_values[0]) > index:
                proficiency = max(0, min(5, round(skill_values[0][index])))
            else:
                # Handle the case where the index is out of bounds
                proficiency = 0  # You may choose a different default value or handle it accordingly

            ApplicantSkill.objects.create(
                applicant=applicant,
                skill=skill,
                proficiency=proficiency
            )

        # Create ApplicantCertificate objects
        for certificate in certificates_list:
            received_at = fake.date_of_birth(minimum_age=20, maximum_age=30)
            expired_at = fake.date_of_birth(minimum_age=25, maximum_age=35) if np.random.choice([True, False]) else None

            ApplicantCertificate.objects.create(
                applicant=applicant,
                certificate=certificate,
                received_at=received_at,
                expired_at=expired_at
            )

        # Create WorkExperience objects
        for exp in work_experience:
            WorkExperience.objects.create(
                applicant=applicant,
                company=exp["company"],
                hired_at=exp["hired_at"],
                left_at=exp["left_at"],
                hired_reason=exp["hired_reason"],
                left_reason=exp["left_reason"],
                role=exp["role"]
            )

        # Add the current applicant to the list
        applicants.append(applicant)

    return applicants


def generate_synthetic_vacancies(num_vacancies, companies, skills, languages, certificates, applicants):
    vacancies = []

    for _ in range(num_vacancies):
        title = fake.job()
        company = np.random.choice(companies)
        location = fake.city()
        salary = np.random.uniform(30000, 100000)
        desired_degree = fake.text()
        required_degree = fake.text()
        role = fake.text()

        # Generate random language proficiencies for the vacancy
        language_proficiencies = {
            language: max(1, int(np.random.normal(3, 1)))
            for language in languages
        }

        # Generate random certificates for the vacancy
        certificates_list = certificates[:np.random.randint(0, len(certificates))]

        # Create a Vacancy object
        vacancy = Vacancy.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            desired_degree=desired_degree,
            required_degree=required_degree,
            role=role
        )

        # Create VacancySkill objects with correlated proficiency levels
        skill_values = np.random.multivariate_normal([4, 4, 4], correlation_matrix, size=1)
        for index, skill in enumerate(skills):
            if len(skill_values[0]) > index:
                desired_proficiency = max(0, min(5, round(skill_values[0][index])))
            else:
                # Handle the case where the index is out of bounds
                desired_proficiency = 0  # You may choose a different default value or handle it accordingly

            required_proficiency = max(0, min(desired_proficiency + random.randint(-1, 1), 5))
            VacancySkill.objects.create(
                vacancy=vacancy,
                skill=skill,
                desired_proficiency=desired_proficiency,
                required_proficiency=required_proficiency
            )

        # Create VacancyLanguage objects
        for language, proficiency in language_proficiencies.items():
            VacancyLanguage.objects.create(
                vacancy=vacancy,
                language=language,
                desired_proficiency=proficiency,
                required_proficiency=proficiency
            )

        # Create VacancyCertificate objects
        for certificate in certificates_list:
            VacancyCertificate.objects.create(
                vacancy=vacancy,
                certificate=certificate,
                required=True
            )

        # Generate synthetic data for the number of applicants who applied to the vacancy
        mean_applicants_applied = np.random.randint(5, 20)
        std_dev_applicants_applied = 2
        num_applicants_applied = int(np.random.normal(mean_applicants_applied, std_dev_applicants_applied))
        num_applicants_applied = max(1, num_applicants_applied)  # Ensure at least 1 applicant
        if num_applicants_applied > len(applicants):
            num_applicants_applied = len(applicants)

        applicants_applied = np.random.choice(applicants, num_applicants_applied, replace=False)

        # Randomly hire a subset of applicants
        num_applicants_hired = np.random.randint(1, num_applicants_applied + 1)
        applicants_hired = np.random.choice(applicants_applied, num_applicants_hired, replace=False)

        # Create VacancyApplication objects
        for applicant in applicants_applied:
            hired_at = timezone.now() if applicant in applicants_hired else None
            left_at = None
            hired_reason = fake.text() if hired_at else None
            left_reason = fake.text() if not hired_at else None

            VacancyApplication.objects.create(
                vacancy=vacancy,
                applicant=applicant,
                hired_at=hired_at,
                left_at=left_at,
                hired_reason=hired_reason,
                left_reason=left_reason
            )

        # Add the current vacancy to the list
        vacancies.append(vacancy)

    return vacancies


def generate_synthetic_data():
    # Generate synthetic data for educational institutes, languages, skills, certificates, and companies
    educational_institutes = generate_synthetic_educational_institutes(num_institutes=5)
    languages = generate_synthetic_languages(num_languages=5)
    skills = generate_synthetic_skills(num_skills=10)
    certificates = generate_synthetic_certificates(num_certificates=5)
    companies = generate_synthetic_companies(num_companies=5)

    # Generate synthetic data for applicants and vacancies
    applicants = generate_synthetic_applicants(num_applicants=10,
                                               institutes=educational_institutes,
                                               languages=languages,
                                               skills=skills,
                                               certificates=certificates,
                                               companies=companies)

    vacancies = generate_synthetic_vacancies(num_vacancies=5,
                                             companies=companies,
                                             skills=skills,
                                             languages=languages,
                                             certificates=certificates,
                                             applicants=applicants)

    response = {}
    # Print the generated synthetic data
    response["educational_institutes"] = []
    for institute in educational_institutes:
        response["educational_institutes"].append(f"{institute.name} - {institute.location}")

    response["languages"] = []
    for language in languages:
        response["languages"].append(language.name)

    response["skills"] = []
    for skill in skills:
        response["skills"].append(skill.name)

    response["certificates"] = []
    for certificate in certificates:
        response["certificates"].append(certificate.name)

    response["companies"] = []
    for company in companies:
        response["companies"].append(f"{company.name} - {company.industry} - {company.size}")

    response["applicants"] = []
    for idx, applicant in enumerate(applicants, 1):
        applicant_response = {"name": f"\nApplicant {idx}: {applicant.name}", "education": []}
        for education in applicant.applicanteducation_set.all():
            applicant_response["education"].append(
                f"- {education.degree} at {education.institute} ({education.started_at} - {education.graduated_at})")

        applicant_response["languages"] = []
        for lang in applicant.applicantlanguage_set.all():
            applicant_response["languages"].append(f"- {lang.language}: {lang.proficiency}/5")

        applicant_response["skills"] = []
        for skill in applicant.applicantskill_set.all():
            applicant_response["skills"].append(f"- {skill.skill}: {skill.proficiency}/5")

        applicant_response["certificates"] = []
        for cert in applicant.applicantcertificate_set.all():
            applicant_response["certificates"].append(
                f"- {cert.certificate} received at {cert.received_at}, expired at {cert.expired_at}")

        applicant_response["work_experience"] = []
        for exp in applicant.workexperience_set.all():
            applicant_response["work_experience"].append(
                f"- {exp.role} at {exp.company} ({exp.hired_at} - {exp.left_at})")

        response["applicants"].append(applicant_response)

    response["vacancies"] = []
    for idx, vacancy in enumerate(vacancies, 1):
        vacancy_response = {"id": idx, "title": vacancy.title, "company": vacancy.company, "salary": vacancy.salary,
                            "required_degree": vacancy.required_degree, "desired_degree": vacancy.desired_degree,
                            "skills": []}

        for skill in vacancy.vacancyskill_set.all():
            vacancy_response["skills"].append(
                f"- {skill.skill}: Desired {skill.desired_proficiency}/5, Required {skill.required_proficiency}/5")

        vacancy_response["languages"] = []
        for lang in vacancy.vacancylanguage_set.all():
            vacancy_response["languages"].append(
                f"- {lang.language}: Desired {lang.desired_proficiency}/5, Required {lang.required_proficiency}/5")

        vacancy_response["certificates"] = []
        for cert in vacancy.vacancycertificate_set.all():
            vacancy_response["certificates"].append(f"- {cert.certificate}: Required")

        vacancy_response["applied"] = []
        for applicant in vacancy.vacancyapplication_set.all():
            vacancy_response["applied"].append(applicant)

        response["vacancies"].append(vacancy_response)

    return response
