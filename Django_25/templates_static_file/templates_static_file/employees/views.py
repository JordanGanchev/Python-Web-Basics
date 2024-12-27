import random
from datetime import datetime

from django.shortcuts import render

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

def index(request):
    contex = {
        'title': 'Employees list',
        "1as": "456", #valid
        # "new.employees": "Jordan" invalid
        # "new employees": "Jordan" invalid
        # "new!employees": "Jordan" invalid
        # "123": "456", invalid

        "person": {
            "first_name": "Jordan",
            "last_name": "Ganchev",
        },
        "person_obj": Person(
            "Jordan",
            "Ganchev"
        ),
        "ll": [1, 2, 3],

        "names": ["Doncho", "Gosho", "Maria"],
        "ages1": [10, 20, 30, 40, 50],
        "ages": [random.randrange(1, 100) for _ in range(10)],
        "date": datetime.today(),
    }

    return render(request, 'employees/index.html', contex)

def employee_details(request, pk):
    context = {
        'pk': pk,
    }
    return render(request, 'employee_details.html', context)
