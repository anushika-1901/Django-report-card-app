from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    address=models.TextField()
    subject1=models.IntegerField()
    subject2=models.IntegerField()
    subject3=models.IntegerField()
    total=models.IntegerField(blank=True,null=True)
    result_date=models.DateField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.total=self.subject1+self.subject2+self.subject3
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name 