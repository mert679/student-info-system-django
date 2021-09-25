from django.db import models

# Create your models here.

class AddStudents(models.Model):
    sdtname = models.CharField(max_length=50)
    sdtid = models.IntegerField()
    sdtclass = models.CharField(max_length=15)
    sdttel = models.CharField(max_length=30)
    sdtemail = models.EmailField(max_length=254)
    sdtday = models.DateField()
    parentname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sdtname}"