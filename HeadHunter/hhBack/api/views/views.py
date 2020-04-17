import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy


# CRUD - For Company Model

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        # option 1
        # company = Company(name=data['name'])
        # company.save()

        # option 2
        company = Company.objects.create(name=data.get('name'))

        return JsonResponse(company.to_json())

@csrf_exempt
def category_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # Get one objects
    if request.method == 'GET':
        return JsonResponse(company.to_json())

    # Update selected objects
    elif request.method == 'PUT':
        data = json.loads(request.body)

        company.name = data.get('name', company.name)
        company.save()

        return JsonResponse(company.to_json())

    # Delete selected object
    elif request.method == 'DELETE':
        company.delete()

        return JsonResponse({'deleted': True})



# CRUD - For Vacancy Model

@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        # option 1
        # vacancy = Vacancy(name=data['name'])
        # vacancy.save()

        # option 2
        vacancy = Vacancy.objects.create(name=data.get('name'))

        return JsonResponse(vacancy.to_json())

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # Get one objects
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())

    # Update selected objects
    elif request.method == 'PUT':
        data = json.loads(request.body)

        vacancy.name = data.get('name', vacancy.name)
        vacancy.save()

        return JsonResponse(vacancy.to_json())

    # Delete selected object
    elif request.method == 'DELETE':
        vacancy.delete()

        return JsonResponse({'deleted': True})