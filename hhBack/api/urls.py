from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.getCompanies),
    path('companies/<int:pk>', views.getCompany),
    path('companies/<int:pk>/vacancies/', views.companyVacancies),
    path('vacancies/', views.getVacancies),
    path('vacancies/<int:pk>/', views.getVacancy),
    path('vacancies/top_ten/', views.topVacancies),
]

