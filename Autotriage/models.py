from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=255)
    deleted = models.IntegerField(default=0)
    insert_date = models.DateField(auto_now=True)
    inserted_by = models.BigIntegerField()

    # def __str__(self):
    #     return self.full_name

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

class CompanyServer(models.Model):
    company_id = models.IntegerField()
    server_os = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
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






