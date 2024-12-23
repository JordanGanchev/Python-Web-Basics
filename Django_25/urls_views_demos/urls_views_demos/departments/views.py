import time
from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Response from {time.time()}")

def index2(request, *args, **kwargs):
    return HttpResponse(f"Response with {args} and {kwargs}")

def department_1_details(request):
    return HttpResponse("Department 1")

def department_2_details(request):
    return HttpResponse("Department 2")

def departments_details(request, pk):
    return HttpResponse(f"Department with ID:{pk}")

def departments_list(request):
    pass

def departments_create(request):
    pass

def departments_details_by_name(request, name):
    return HttpResponse(f"Department with name: {name}")

#---------------------------------------------------------
# Function base view

# def index(request):
#     return HttpResponse("It work")
#
# def index(request, *args, **kwargs):
#     return HttpResponse(f"It work with args={args} and kwargs={kwargs}")