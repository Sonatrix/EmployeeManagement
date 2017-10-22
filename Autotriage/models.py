from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import models as auth_models

class Employee(AbstractUser):
    designation = models.CharField(max_length=100)
    inserted_by = models.BigIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.designation

class Company(models.Model):
    pid = models.IntegerField(default=0)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    is_company = models.BooleanField()
    is_contact = models.BooleanField()
    added_date = models.DateField(auto_now=True)
    added_by = models.IntegerField()
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name

class Branch(models.Model):
    pid = models.IntegerField(default=1)
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(max_length=255)
    added_date = models.DateField(auto_now=True)
    added_by = models.IntegerField()
    deleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    branch = models.ForeignKey(Branch)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=240,blank=True, null=True)
    added_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    
class CompanyServer(models.Model):
    company_id = models.IntegerField()
    server_os = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    branch = models.ForeignKey(Branch)
    password = models.CharField(max_length=500)
    server_name = models.CharField(max_length=255)
    public_ip = models.CharField(max_length=100)
    private_ip = models.CharField(max_length=100)
    alert_sender_email1 = models.EmailField(max_length=100)
    alert_sender_email2 = models.EmailField(max_length=100, blank=True)
    alert_sender_email3 = models.EmailField(max_length=100, blank=True)
    escalate_to_email1 = models.EmailField(max_length=100)
    escalate_to_email2 = models.EmailField(max_length=100, blank=True)
    added_date = models.DateField(auto_now=True)
    added_by = models.IntegerField()
    deleted = models.IntegerField()


class Email(models.Model):
    email = models.EmailField(max_length=250,null=False,blank=False)
    password = models.CharField(max_length=250, null=False, blank=False)
    pop_server_name = models.CharField(max_length=200,null=False,blank=True)
    pop_port = models.IntegerField(blank=False,null=False)
    imap_server_name = models.CharField(max_length=200, null=False, blank=True)
    imap_port = models.IntegerField(blank=False, null=False)
    added_date = models.DateField(auto_now=True)
    added_by = models.IntegerField()
    deleted = models.IntegerField()
    

    






