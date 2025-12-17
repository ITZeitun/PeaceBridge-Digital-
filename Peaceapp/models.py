from django.db import models

class Donation(models.Model):
    contact = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact} donated {self.amount}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
