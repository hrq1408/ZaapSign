from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)

class Document(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    open_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Signer(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=50)
    token = models.CharField(max_length=255)
