from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from detect.models import Student, Employee, Person, DetectedCriminal
from django.db.models import Count
from django.http import JsonResponse

@login_required
def index(request):
    numberOfStudents = Student.objects.count()
    numberOfEmployees = Employee.objects.count()
    numberOfCriminals = Person.objects.filter(status = 'WANTED').count()
    numberOfPeople = Person.objects.count()
    people = Person.objects.all()
    detectedCriminal = DetectedCriminal.objects.all()
    wanted = Person.objects.filter(status='WANTED').count()
    unwanted = Person.objects.filter(status='NOT WANTED').count()
    male = Person.objects.filter(gender="Male").count()
    female = Person.objects.filter(gender="Female").count()

    context = {
        'numberOfStudents' : numberOfStudents,
        'numberOfEmployees' : numberOfEmployees,
        'numberOfCriminals' : numberOfCriminals,
        'numberOfPeople' : numberOfPeople,
        'people' : people,
        'detectedCriminal' : detectedCriminal,
        'wanted' : wanted,
        'unwanted' : unwanted,
        'male' : male,
        'female' : female,

    }
    return render(request, "index.html", context)

def home(request):
    return render(request, "home.html")