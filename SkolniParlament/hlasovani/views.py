from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Student,Kandidat,Vitezove

#test-smažem
def hlasovanitest(request):
    all_students= Student.objects.all()
    html=''
    for student in all_students:
        url='/hlasovani/'+student.token+'/'
        vypisStudent=str(student.jmeno)
        html+='<a href="'+url+'">'+vypisStudent+'</a><br>'
    return HttpResponse(html)

#test-smažem
def kandidovattest(request):
    all_students= Kandidat.objects.all()
    html=''
    for student in all_students:
        url='/kandidovat/'+student.Student.token+'/'
        vypisStudent=str(student.Student.jmeno)
        html+='<a href="'+url+'">'+vypisStudent+'</a><br>'
    return HttpResponse(html)



def hlasovani(request, Student_token):
    tokenMajitel = Student.objects.get(token=Student_token)
    vybranaTrida=tokenMajitel.trida
    if tokenMajitel.voted==False:
        vybrani = Student.objects.filter(trida=vybranaTrida)
        template = loader.get_template('hlasovani/hlasovani.html')
        context = {
            'vybrani': vybrani,
            'tokenMajitel': tokenMajitel,
        }
        return HttpResponse(template.render(context, request))
    else :
        return HttpResponse('<h1>ty už jsi volil koblížku</h1>')





def kandidovat(request, Kandidat_token):
    vybranej = Student.objects.get(token=Kandidat_token)
    template = loader.get_template('hlasovani/kandidovat.html')
    context = {
        'vybranej': vybranej,
    }
    return HttpResponse(template.render(context, request))



def vysledky(request):
    vitezove=Vitezove.objects.all()
    context={'vitezove':vitezove,
             }

    return render(request,'hlasovani/vysledky.html',context)
