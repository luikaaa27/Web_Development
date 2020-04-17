from django.urls import path
from api.views.views_fbv import company_list,company_detail,vacancy_by_company,vacancy_detail,topVacancies,vacancy_list
from api.views.views_cbv import CompanyListAPIView, CompanyDetailAPIView, VacancyDetailAPIView, VacancyListAPIView, \
    TopVacanciesAPIView, VacancyByCompanyAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('companies/', company_list),
    # path('companies/<int:company_id>/', company_detail),
    # path('companies/<int:company_id>/vacancies/', vacancy_by_company),
    # path('vacancies/', vacancy_list),
    # path('vacancies/<int:company_id>/', vacancy_detail),
    # path('vacancies/top_ten/', topVacancies),

    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:company_id>/vacancies/', VacancyByCompanyAPIView.as_view()),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', TopVacanciesAPIView.as_view()),

    path('login/', obtain_jwt_token),

]

