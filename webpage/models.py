from django.db import models

# Create your models here.
class Position(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        phone = models.CharField(max_length=100)
        company_name = models.CharField(max_length=100)
        where_did_you_find_us = models.CharField(max_length=100)
        applyfor = models.CharField(max_length=100)
        website_url = models.CharField(max_length=100)
        message = models.CharField(max_length=100)
        file = models.FileField(blank=True, null=True)

class Projects(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        phone = models.CharField(max_length=100)
        company_name = models.CharField(max_length=100)
        where_did_you_find_us = models.CharField(max_length=100)
        budget = models.CharField(max_length=100)
        website_url = models.CharField(max_length=100)
        message = models.CharField(max_length=100)
        file = models.FileField(blank=True, null=True)