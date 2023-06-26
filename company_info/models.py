from django.db import models

# Create your models here.

# class startup_ranking(models.Model):
#     logo = models.CharField(max_length=100,db_column='logo')
#     ranking = models.CharField(max_length=15,db_column='ranking')
#     company_name = models.CharField(max_length=100,db_column='company_name')
#     recap = models.CharField(max_length=100,db_column='recap')


class Company_list(models.Model):
    com_png = models.CharField(max_length=100)
    com_rank = models.CharField(max_length=7)
    com_name = models.CharField(max_length=100)
    com_in = models.TextField()


    def __str__(self):
        return f'{self.com_rank}   -   {self.com_name}'