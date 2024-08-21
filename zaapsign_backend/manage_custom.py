from django.db import models

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
