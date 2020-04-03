from django.shortcuts import render
from api.models import Company, Vacancy
from django.http import Http404, JsonResponse


def getCompanies(request):
    companies = Company.objects.all()
    json_companies = [company.to_json() for company in companies]
    return JsonResponse(json_companies, safe=False)

def getCompany(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(company.to_json())

def companyVacancies(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    vacancies = company.vacancy_set.all()
    json_vacancies = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def getVacancies(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def getVacancy(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    return JsonResponse(vacancy.to_json())

def topVacancies(request):
    tenVacancies = sorted(Vacancy.objects.all(),key = Vacancy.getSalary,reverse=True)[:10]
    json_vacancies = [vacancy.to_json() for vacancy in tenVacancies]
    return JsonResponse(json_vacancies, safe=False)
