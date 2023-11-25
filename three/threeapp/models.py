from django.db import models
#from threeapp.manager import CustomManager

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=100)
    date=models.DateField()
    uid=models.IntegerField()
    is_deletes=models.CharField(max_length=10)

    def __str__(self):
        return self.id



class Course(models.Model):
    cname=models.CharField(max_length=40)
    cdur=models.IntegerField()
    ccat=models.CharField(max_length=40)
    cprice=models.IntegerField()

    def __str__(self):
        return self.title


    #obj=models.Manager()
    #ccustomobj=CustomManager()



