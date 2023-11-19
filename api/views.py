# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
import json
from django.core import serializers

from api.models import Applicant, Vacancy
from api.serializers.applicant_serializer import ApplicantSerializer, VacancySerializer


def export_data_applicants(request):
    # Fetch data for the Applicant model and related models
    applicants = ApplicantSerializer(Applicant.objects.all(), many=True).data

    # Convert the list to JSON
    json_data = json.dumps(applicants, cls=DjangoJSONEncoder, indent=2)

    # Create a response with the JSON data
    response = HttpResponse(json_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=applicants_data.json'

    return response


def export_data_vacancies(request):
    # Fetch data for the Applicant model and related models
    vacancies = VacancySerializer(Vacancy.objects.all(), many=True).data

    # Convert the list to JSON
    json_data = json.dumps(vacancies, cls=DjangoJSONEncoder, indent=2)

    # Create a response with the JSON data
    response = HttpResponse(json_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=vacancies_data.json'

    return response


def home(request):
    return render(request, 'home.html')
