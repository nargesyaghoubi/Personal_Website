
from django.shortcuts import render
from .models import *


def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    academics = Academy.objects.all()
    courses = Course.objects.all()
    basics = Basic.objects.all()



    context ={
        'skills': skills,
        'projects': projects,
        'academics': academics,
        'courses': courses,
        'basics': basics,
    }
    return render(request, template_name='index.html', context=context)










