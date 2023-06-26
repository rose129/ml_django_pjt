from django.db import models

# Create your models here.

class startup_ranking(models.Model):
    logo = models.CharField(max_length=100,db_column='logo')
    ranking = models.CharField(max_length=15,db_column='ranking')
    company_name = models.CharField(max_length=100,db_column='company_name')
    recap = models.CharField(max_length=100,db_column='recap')
