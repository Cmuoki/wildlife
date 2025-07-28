from django.db import models

class Tourist(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    date = models.DateField()
    phone = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=100)
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='places/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


