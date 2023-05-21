from django.db import models

# Create your models here.
class employee(models.Model):
    Id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    Salary=models.IntegerField(null=True,blank=True)

class Department(models.Model):
    Dep_id=models.IntegerField(primary_key=True)
    Dep_name=models.CharField(max_length=50,null=True,blank=True)