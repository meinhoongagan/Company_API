from django.db import models

# Create company models here.
class Company(models.Model):
    name = models.CharField( max_length=100)
    company_id=models.AutoField(primary_key = True)
    location=models.CharField( max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),("Non IT","Non IT"),("Mobile Phones","Mobile Phones")))
    created_at=models.DateTimeField( auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name + "("+self.location+")"
class Employee(models.Model):
    name = models.CharField( max_length=100)
    email=models.CharField( max_length=50)
    address=models.CharField (max_length=200)
    phone=models.CharField( max_length=10)
    about=models.TextField()
    position=models.CharField( max_length=50,choices=(("Manager","Manager"),("Software Developer","Software Developer"),("Project Leader","Project Leader")))
    company=models.ForeignKey(Company, related_name="employee", on_delete=models.CASCADE)

    def __str__(self):
        return self.name 