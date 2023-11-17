# Synthetic Hiring Data Generator

This Django application is designed to generate synthetic hiring data for testing and development purposes. The application exposes the Django admin interface for manual data management and includes scripts for generating and downloading synthetic data in CSV format.

## Table of Contents
- Installation
- Usage
  - Django Admin
  - Data Generation
  - Data Download
- Models

## Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/synthetic-hiring-data-generator.git
```

2. Go to the project directory
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Apply the migrations:
```bash
python manage.py migrate
```
5. Create a super User for Django Admin:
```bash
python manage.py createsuperuser
```
6. Follow the promts to create a super user.
7. Start the development server
```bash
python manage.py runserver
```
8. Open your browser and navigate to http://127.0.0.1:8000/admin/. 
9. Log in with the superuser credentials created in step 6.

## Usage
### Admin Panel
- Access the Django admin interface at http://127.0.0.1:8000/admin/.
- Use the admin interface to manually manage the hiring data, including applicants, vacancies, companies, languages, skills, certificates, educational institutes, and more.

### Data Generation
- On the home screen, find a button labeled "Generate Data."
- Clicking this button triggers a script that generates synthetic hiring data and populates the database.

### Data Download
- On the home screen, find a button labeled "Download Data as CSV."
- Clicking this button triggers a script that exports the generated data to a CSV file, which is then available for download.

## Models

The application uses the following models to represent hiring data:
### Main Models
- EducationalInstitute
- Language
- Skill
- Certificate
- Company
- Applicant
- Vacancy

### Pivot Tables
- ApplicantLanguage
- ApplicantEducation
- ApplicantSkill
- ApplicantCertificate
- WorkExperience
- VacancySkill
- VacancyLanguage
- VacancyCertificate
- VacancyApplication

Refer to the models.py in `synhire` for detailed information about each model and their relationships.