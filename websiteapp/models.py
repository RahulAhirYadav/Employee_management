from django.db import models


# Create your models here.
class Department (models.Model):
    name =  models.CharField(max_length=50)
    description =  models.TextField()

    def __str__(self):
        return self.name
ats=(('Active','Active'),('Inactive','Inactive'))   
class Employee (models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    dob = models.DateField()
    email= models.EmailField(max_length=50)
    working_time= models.CharField(max_length=50)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    salary= models.IntegerField(null='true',blank='true')
    status=models.CharField(max_length=10,choices=ats,default="Active")


    def __str__(self):
        return self.firstname +" "+ self.lastname 

class EmpAttendence(models.Model):
    employee = models.ForeignKey(Employee ,on_delete=models.CASCADE)
    department_name = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    date = models.DateField()
    present_status = models.CharField(max_length=50)

class TrainingMaster (models.Model):
    trainingtype = models.CharField(max_length=50)
    trainingdescription =  models.TextField(max_length=50)
    trainingduration =  models.CharField(max_length=50)

    def __str__(self):
        return self.trainingtype

class EmpTraining (models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    trainingtype = models.ForeignKey(TrainingMaster,on_delete=models.CASCADE)
    startdate = models.CharField(max_length=50)
    enddate = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)

class Company (models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=100) 


class Contact(models.Model):
    name =  models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()    
    





   
              
    




    


