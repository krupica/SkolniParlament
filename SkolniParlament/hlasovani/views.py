from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Student,Kandidat,Vitezove
from django.db.models import F

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
    all_students= Student.objects.all()
    html=''
    for student in all_students:
        url='/kandidovat/'+student.token+'/'
        vypisStudent=str(student.jmeno)
        html+='<a href="'+url+'">'+vypisStudent+'</a><br>'
    return HttpResponse(html)



def hlasovani(request, Student_token):
    tokenMajitel = Student.objects.get(token=Student_token)
    vybranaTrida=tokenMajitel.trida
    if tokenMajitel.voted==False:
        if request.GET.get('tunatoto'):
            kandId = (request.GET.get('tunatoto'))
            yey = Kandidat.objects.filter( Student__id__contains=kandId)  # kandidat_ pred id__contains
            yey.update(votes=F('votes') + 1)
            print(yey)
            tokenMajitel.voted = True
            tokenMajitel.save()
            return HttpResponse('<h1>ÚSPĚŠNĚ ODESLÁNO</h1>')
        vybrani = Student.objects.filter( kandidat__Student__trida__contains=vybranaTrida)
        template = loader.get_template('hlasovani/hlasovani.html')
        context = {
            'vybrani': vybrani,
            'tokenMajitel': tokenMajitel,
        }
        return HttpResponse(template.render(context, request))
    else :
        return HttpResponse('<h1>ty už jsi volil koblížku</h1>')




def kandidovat(request, Kandidat_token):
    print(Kandidat_token)
    if not Kandidat.objects.filter( Student__token__contains=Kandidat_token):
        if request.GET.get('potvrzeno'):
            studId = (request.GET.get('potvrzeno'))
            student = Student.objects.get( id__contains=studId)
            kandidat = Kandidat()
            kandidat.Student = student
            kandidat.save()
            return HttpResponse('<h1>ÚSPĚŠNĚ ODESLÁNO</h1>')
        vybranej = Student.objects.get(token=Kandidat_token)
        template = loader.get_template('hlasovani/kandidovat.html')
        context = {
            'vybranej': vybranej,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse('<h1>ty už jsi kandidát koblížku</h1>')



def vysledky(request):
    vitezove=Vitezove.objects.all()
    context={'vitezove':vitezove,
             }

    return render(request,'hlasovani/vysledky.html',context)

