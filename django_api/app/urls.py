# yourapp/urls.py
from django.urls import path
from .views import total_records, mean_salary, median_salary

urlpatterns = [
    path('total_records/', total_records, name='total_records'),
    path('mean_salary/', mean_salary, name='mean_salary'),
    path('median_salary/', median_salary, name='median_salary'),
    # path('percentile_salary/<int:percentile>/', percentile_salary, name='percentile_salary'),
]
