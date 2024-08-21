from django.db import models
from companies.models import Company

class Document(models.Model):
    name = models.CharField(max_length=255)
    open_id = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Signer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    document = models.ForeignKey(Document, related_name='signers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.email})"
