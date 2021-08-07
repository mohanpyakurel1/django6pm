from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    subject=models.TextField()
    message=models.TextField()
    def __str__(self):
        return f"{self.name} has sent you message"
class Info(models.Model):
    address= models.CharField(max_length=300)
    local_address= models.CharField(max_length=300)
    phone=models.CharField(max_length=200)
    time= models.CharField(max_length=300)
    email=models.CharField(max_length=200)
    def __str__(self):
        return self.address