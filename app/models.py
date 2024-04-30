from django.db import models

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    email = models.CharField(max_length=30, blank=False ,unique=True)
    password = models.CharField(max_length=30, blank=False)
    phno = models.CharField(max_length=30, blank=False, unique=True)
    class Meta:
        db_table = "register_table"
