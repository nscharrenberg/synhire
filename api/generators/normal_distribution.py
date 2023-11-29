import random
import numpy as np
from faker import Faker
from django.utils import timezone
from faker_education import SchoolProvider
from scipy.linalg import cholesky

from api.models import (EducationalInstitute, Language, Skill, Certificate, Company,
                        Applicant, Vacancy, ApplicantLanguage, ApplicantSkill,
                        ApplicantCertificate, WorkExperience, ApplicantEducation,
                        VacancySkill, VacancyLanguage, VacancyCertificate, VacancyApplication)

# Set seed for reproducibility
np.random.seed(42)

fake = Faker()
fake.add_provider(SchoolProvider)

NUM_LANGUAGES = 3
NUM_INSTITUTES = 5
NUM_SKILLS = 20
NUM_CERTIFICATES = 5
NUM_COMPANIES = 30
NUM_APPLICANTS = 100
NUM_VACANCIES = 10

MAX_ATTEMPTS = 1000


def ensure_positive_semidefinite(matrix):
    try:
        # Attempt Cholesky decomposition
        cholesky_factor = np.linalg.cholesky(matrix)
    except np.linalg.LinAlgError:
        # Eigenvalue adjustment if Cholesky fails
        eigvals, eigvecs = np.linalg.eigh(matrix)
        adjusted_eigvals = np.maximum(eigvals, 0.01)  # Adjust with a small positive constant
        adjusted_cov_matrix = eigvecs @ np.diag(adjusted_eigvals) @ eigvecs.T
        cholesky_factor = np.linalg.cholesky(adjusted_cov_matrix)

    return cholesky_factor


def generate_synthetic_educational_institutes(num_institutes):
    return [EducationalInstitute.objects.create(name=fake.school_name(), location=fake.school_district()) for _ in
            range(num_institutes)]


def generate_synthetic_languages(num_languages):
    return [Language.objects.create(name=fake.country()) for _ in range(num_languages)]


def generate_synthetic_skills(num_skills):
    return [Skill.objects.create(name=fake.domain_word()) for _ in range(num_skills)]


def generate_synthetic_certificates(num_certificates):
    return [Certificate.objects.create(name=fake.cryptocurrency_name()) for _ in range(num_certificates)]


def generate_synthetic_companies(num_companies):
    return [Company.objects.create(
        name=fake.company(),
        size=np.random.randint(1, 1000),
        revenue=np.random.uniform(100000, 100000000),
        industry=fake.color_name(),
        rating=np.random.uniform(1, 5),
        description=fake.catch_phrase()
    ) for _ in range(num_companies)]


def generate_synthetic_applicants(num_applicants, institutes, languages, skills, certificates, companies, mean_vector, correlation_matrix):
    applicants = []

    for _ in range(num_applicants):
        # Generate random applicant name
        name = fake.name()

        # Randomly choose an educational institute
        institute = np.random.choice(institutes)

        # Generate random education details
        started_at = fake.date_of_birth(minimum_age=20, maximum_age=30)
        graduated_at = fake.date_of_birth(minimum_age=25, maximum_age=35) if np.random.choice([True, False]) else None
        degree = fake.cryptocurrency_code()

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
            role = fake.job()

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
        skill_values = np.random.multivariate_normal(mean_vector, correlation_matrix, size=1)
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


def generate_synthetic_vacancies(num_vacancies, companies, skills, languages, certificates, applicants, mean_vector, correlation_matrix):
    vacancies = []

    for _ in range(num_vacancies):
        title = fake.job()
        company = np.random.choice(companies)
        location = fake.city()
        salary = np.random.uniform(30000, 100000)
        desired_degree = fake.cryptocurrency_code()
        required_degree = fake.cryptocurrency_code()
        role = fake.job()

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
        skill_values = np.random.multivariate_normal(mean_vector, correlation_matrix, size=1)
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

        # Identify the applicant with the highest skill proficiency
        best_fit_applicant = max(applicants_applied, key=lambda applicant1: sum(
            [skill1.proficiency for skill1 in applicant1.applicantskill_set.all()]))

        # Randomly hire a subset of applicants, ensuring the best fit applicant is hired
        num_applicants_hired = np.random.randint(1, num_applicants_applied + 1)
        applicants_hired = np.random.choice(applicants_applied, num_applicants_hired - 1, replace=False)
        applicants_hired = np.append(applicants_hired, best_fit_applicant)

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
    # Generate a random correlation matrix
    mean_vector = np.random.uniform(low=1, high=5, size=NUM_SKILLS)  # Adjust the low and high values as needed
    correlation_matrix = np.random.uniform(low=0.5, high=1, size=(NUM_SKILLS, NUM_SKILLS))

    # Make the matrix symmetric
    correlation_matrix = 0.5 * (correlation_matrix + correlation_matrix.T)

    # Set diagonal elements to 1
    np.fill_diagonal(correlation_matrix, 1.0)

    # Ensure positive semi-definite correlation matrix
    correlation_matrix = ensure_positive_semidefinite(correlation_matrix)

    # Generate synthetic data for educational institutes, languages, skills, certificates, and companies
    educational_institutes = generate_synthetic_educational_institutes(num_institutes=NUM_INSTITUTES)
    languages = generate_synthetic_languages(num_languages=NUM_LANGUAGES)
    skills = generate_synthetic_skills(num_skills=NUM_SKILLS)
    certificates = generate_synthetic_certificates(num_certificates=NUM_CERTIFICATES)
    companies = generate_synthetic_companies(num_companies=NUM_COMPANIES)

    # Generate synthetic data for applicants and vacancies
    applicants = generate_synthetic_applicants(num_applicants=NUM_APPLICANTS,
                                               institutes=educational_institutes,
                                               languages=languages,
                                               skills=skills,
                                               certificates=certificates,
                                               companies=companies,
                                               mean_vector=mean_vector,
                                               correlation_matrix=correlation_matrix)

    vacancies = generate_synthetic_vacancies(num_vacancies=NUM_VACANCIES,
                                             companies=companies,
                                             skills=skills,
                                             languages=languages,
                                             certificates=certificates,
                                             applicants=applicants,
                                             mean_vector=mean_vector,
                                             correlation_matrix=correlation_matrix)

    return "Done"
