from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg, Count

from .models import H1BApplicant

# Create your views here.
def index(request):
    return render(request,"index.html")

# yourapp/views.py

def total_records(request):
    total_records_count = H1BApplicant.objects.count()
    return JsonResponse({'total_records': total_records_count})

def mean_salary(request):
    mean_salary = H1BApplicant.objects.aggregate(avg_salary=Avg('salary'))
    return JsonResponse({'mean_salary': mean_salary['avg_salary']})

def median_salary(request):
    median_salary = H1BApplicant.objects.order_by('salary')[H1BApplicant.objects.count() // 2].salary
    return JsonResponse({'median_salary': median_salary})

# def percentile_salary(request, percentile):
#     percentile_salary = H1BApplicant.objects.percentile(percentile, field='salary')
#     return JsonResponse({f'{percentile}_percentile_salary': percentile_salary})
