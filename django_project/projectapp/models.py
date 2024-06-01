from django.db import models



class Datas(models.Model):
    gender_choices=[
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    ]
      
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Contact=models.IntegerField(default="")
    Address=models.CharField(max_length=50,default="")
    Mail=models.CharField(max_length=50,default="")
    Gender=models.CharField(choices=gender_choices,null=True,blank=True,max_length=50)

# Create your models here.
