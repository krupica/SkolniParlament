from django.http import HttpResponse
from .models import Student,Kandidat,Vitezove
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import DataFile


def hlasovani(request, Student_token):
    vybranej=Student.objects.filter(Student.token==Student_token)

    template=loader.get_template('hlasovani/hlasovani.html')
    context={
        'vybranej': vybranej,
    }
    html='hlasovani'
    return HttpResponse(template.render(context,request))


def kandidovat(request, Student_token):
    return HttpResponse('<h1>zaskrtnuti kandidovani<h1>')


def vysledky(request):
    return HttpResponse("<h1>vysledky<h1>")