from django.db import models


class Student(models.Model):
    jmeno = models.CharField(max_length=30)
    prijmeni = models.CharField(max_length=30)
    trida = models.CharField(max_length=10)
    email = models.CharField(max_length=70)
    token = models.CharField(max_length=50)
    voted = models.CharField(max_length=3,default='NO')

    def __str__(self):
        return self.jmeno + '-' + self.prijmeni + '-' + self.trida + '-' + self.email + '-' + self.token+'-'+self.voted


class Kandidat(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Student + '-' + self.votes


class Vitezove(models.Model):
    Kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE)

    def __str__(self):
        return self.Kandidat

class DataFile(models.Model):
    name = models.CharField(max_length=50)
    data = models.FileField(upload_to='uploaded_files')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print("Saving this shit")

        super(DataFile, self).save()
        print("Saved")

        file_process(self.data.url)

def file_process(file=None):

    print("Tak schvalne : ", file)

    with open(file) as f:
        linky = f.read().split("\n")
        for line in linky:
            data_dict = {}
            neco = line.split(";")
            print(neco[0])
            print(neco[1])
            print(neco[2])
            print(neco[3])
            try:
                data_dict["jmeno"] = neco[0]
                data_dict["prijmeni"] = neco[1]
                data_dict["trida"] = neco[2]
                data_dict["email"] = neco[3]
                # form = Student(data_dict)
                # print(form)
                # form.save()
            except IndexError:
                print("Spatny index")
    print("hotovo")



