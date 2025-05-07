from django.db import models
import datetime
from ckeditor.fields import RichTextField


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contact'

    icon = models.CharField(max_length=30, blank=True)
    web_title = models.CharField(max_length=120, blank=True)
    map = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='photos/', blank=True)
    phone = models.TextField(blank=True)
    linkedine = models.TextField(blank=True)
    github = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return 'Narges'


class Skill(models.Model):
    title = models.CharField(max_length=40, blank=True)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.title} ({self.percent}%)'


class Project(models.Model):
    icon = models.CharField(max_length=30, blank=True)
    title = RichTextField(max_length=50, blank=True)
    text = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Academy(models.Model):
    class Meta:
        verbose_name_plural = 'Academics'

    icon = models.CharField(max_length=30, blank=True)
    title = RichTextField(max_length=50, blank=True)
    year = models.CharField(max_length=15, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Course(models.Model):
    class Meta:
        verbose_name_plural = 'Courses'

    title = models.CharField(max_length=70, blank=True)
    text = RichTextField(blank=True)
    image = models.ImageField(upload_to='photos/course/', blank=True)
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.id} - {self.title} ({self.date})'

class Basic(models.Model):
    class Meta:
        verbose_name_plural = 'Basics'
    title: models.CharField( max_length=100, blank=True)
    phone: models.CharField(max_length=20, blank=True)
    email: models.EmailField(blank=True)
    twitter = models.TextField(blank=True)
    facebook = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)
    pinterest = models.TextField(blank=True)
    github: models.TextField(blank=True)
    footer = RichTextField(blank=True)

    def __str__(self):
        return self.title













