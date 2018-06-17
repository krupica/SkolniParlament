from django.core.mail import send_mail
from django.db import models
from django.db.models import Max
from django.db.models.functions import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from django.conf import settings
from uuid import uuid4
from threading import Thread
import time

# Create your models here.
class Student(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    trida = models.CharField(max_length=10)
    email = models.CharField(max_length=70)
    token = models.CharField(max_length=50, blank=True)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return ("{} {} {}".format(self.jmeno, self.prijmeni, self.trida))


class Kandidat(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.Student, self.votes)


class Vitezove(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    trida = models.CharField(max_length=10)
    votes = models.IntegerField(default=0)
    datum = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return ("{} {} {} {}".format(self.jmeno, self.prijmeni, self.trida, self.votes))


class DataFile(models.Model):
    nazev = models.CharField(max_length=50)
    soubor = models.FileField(upload_to='uploaded_files')
    konec_kandidovani = models.DateTimeField()
    konec_hlasovani = models.DateTimeField()

    def __str__(self):
        return self.nazev

    def save(self, *args, **kwargs):
        print("Saving this shit")

        super(DataFile, self).save()
        print("Saved")

        file_process(self.soubor.url)
        ukoncit_cokoliv(self.konec_kandidovani, self.konec_hlasovani)


def file_process(file=None):

    Student.objects.all().delete()

    with open(file) as f:
        linky = f.read().split("\n")
        for line in linky:
            data_dict = {}
            neco = line.split(";")
            try:
                stud = Student()
                stud.jmeno = neco[0]
                stud.prijmeni = neco[1]
                stud.trida = neco[2]
                stud.email = neco[3]
                stud.token = uuid4()
                stud.save()
            except IndexError:
                # tohle je tu schvalne
                pass
        print("Parsovani dokonceno")


def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    return decorator


@postpone
def ukoncit_cokoliv(konec_kandidovani, konec_hlasovani):
    main = konec_kandidovani
    mail("kandidovat")
    while True:
        if timezone.now() >= main:
            print("ya all shit")
            if main != konec_hlasovani:
                # udela se to co se ma udelat po konci kandidovani
                print("konec kandidatury...")
                mail("hlasovani")
                main = konec_hlasovani
            else:
                # udela se to co se ma udelat po konci hlasovani
                print("konec hlasovani...")
                res = Kandidat.objects.values('Student__trida').annotate(votes=Max('votes'))
                for trida in res:
                    aqswe = Kandidat.objects.filter(Student__trida=trida['Student__trida'], votes=trida['votes'])[0]
                    vitez = Vitezove()
                    vitez.jmeno=aqswe.Student.jmeno
                    vitez.prijmeni=aqswe.Student.prijmeni
                    vitez.trida=aqswe.Student.trida
                    vitez.votes=aqswe.votes
                    vitez.save()
                mail("vysledky")
                break
        else:
            time.sleep(10)
            pass



@postpone
def mail(faze):
    all_students = Student.objects.all()
    for student in all_students:
        subject = "Volby do studentského parlamentu vole - "+faze
        from_email = settings.EMAIL_HOST_USER
        to_email = [student.email]
        message = "http://127.0.0.1:8000/" + faze + "/" + student.token
        if faze == "vysledky":
            message = "http://127.0.0.1:8000/" + faze
        send_mail(subject, message, from_email, to_email, fail_silently=False)