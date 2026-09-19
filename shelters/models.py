from django.db import models

class Shelter(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    capacity = models.IntegerField()
    is_open = models.BooleanField(default=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PendingCheckin(models.Model):
    STATUS_CHOICES = [
        ('OK', 'OK'),
        ('NEED_HELP', 'Need Help'),
        ('SOS', 'SOS'),
    ]

    device_id = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    battery_level = models.FloatField()
    created_at = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} at {self.created_at}"