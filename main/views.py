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
    services = Service.objects.all()
    academics = Academy.objects.all()
    basics = Basics.objects.all()
    posts = Blog.objects.order_by('-date')[:4]

    context ={
        'skills': skills,
        'services': services,
        'academics': academics,
        'basics': basics,
        'posts' : posts
    }
    return render(request, template_name='index.html', context=context)










