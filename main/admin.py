from django.contrib import admin

from .models import *

class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'percent']
    list_display_links = ['id','title']
    list_editable = ['percent']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon']
    list_display_links = ['id','title']
    list_editable = ['icon']

class AcademyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon']
    list_display_links = ['id','title']
    list_editable = ['icon']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_display_links = ['id', 'title', 'date']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Academy, AcademyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Contact)



