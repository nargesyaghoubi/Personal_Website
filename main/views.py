# from django.shortcuts import render
# from .models import Skill, Project, Experience
#
# def index(request):
#     skills: Skill.objects.all()
#     projects: Project.objects.all()
#     Experiences: Experience.objects.all()
#     context = {
#         'skills': Skill,
#         'projects': Project,
#         'Experiences': Experience,
#     }
#     return render(request, template_name='index.html', context=context)


from django.shortcuts import render
from .models import *


def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    academics = Academy.objects.all()
    courses = Course.objects.all()
    # posts = Course.objects.order_by('-date')[:4]

    context ={
        'skills': skills,
        'projects': projects,
        'academics': academics,
        'courses': courses,
        # 'posts': posts
    }
    return render(request, template_name='index.html', context=context)










