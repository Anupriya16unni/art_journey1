from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=40)

    class Meta:
        db_table="admin_login"

