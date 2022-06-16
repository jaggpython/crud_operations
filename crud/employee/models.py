from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  