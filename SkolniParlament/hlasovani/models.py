from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from uuid import uuid4

# Create your models here.
class Student(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    trida = models.CharField(max_length=10)
    email = models.CharField(max_length=70)
    token = models.CharField(max_length=50, blank=True)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return ("{} {} {} {}".format(self.jmeno, self.prijmeni, self.trida, self.token))


class Kandidat(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Student) + '-' + str(self.votes)


class Vitezove(models.Model):
    Kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Kandidat)

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


def file_process(file=None):

    print("Tak schvalne : ", file)

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
                print("Spatny index")
        print("Parsovani dokonceno")




