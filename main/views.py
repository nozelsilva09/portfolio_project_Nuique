# Create your views here.

from django.shortcuts import render
from .models import Project, Skill

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'main/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def education(request):
    return render(request, 'main/education.html')

def contact(request):
    return render(request, 'main/contact.html')




id="k7b92z"
from django.shortcuts import render
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(name, email, message)  # for now (shows in terminal)

    return render(request, 'main/contact.html')