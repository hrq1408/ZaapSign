from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)

class Document(models.Model):    
    PENDING = 'Pending'
    SIGNED = 'Signed'
    REJECTED = 'Rejected'

    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SIGNED, 'Signed'),
        (REJECTED, 'Rejected'),
    ]

    name = models.CharField(max_length=255)
    open_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Signer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    document = models.ForeignKey(Document, related_name='signers', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')
    token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

