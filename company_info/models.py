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
    industry_field = models.CharField(max_length=100)
    workforce = models.CharField(max_length=40)
    com_detail_type = models.CharField(max_length=30)
    est_date = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    sales = models.CharField(max_length=50)
    ceo = models.CharField(max_length=30)
    initial_salary = models.CharField(max_length=30)
    main_business = models.CharField(max_length=200)
    insurance = models.CharField(max_length=50)
    website = models.CharField(max_length=60)
    com_detail_address = models.CharField(max_length=170)
    subsidiary = models.CharField(max_length=270)

    def __str__(self):
        return f'{self.com_rank}   -   {self.com_name}'

    def get_absolute_url(self):
        return f'/company_info/{self.com_name}'

class Ml_final(models.Model):
    com_name = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)

    def __str__(self):
         return f'{self.com_name}   -   {self.rating}'
    


# class CompanyReview(models.Model):
#     re_com_name = models.CharField(max_length=20)
#     re_date = models.CharField(max_length=50)
#     re_job = models.CharField(max_length=15)
#     re_working_status = models.CharField(max_length=4)
#     re_rating = models.IntegerField()
#     re_recap = models.TextField()
#     re_merit = models.TextField()
#     re_demerit = models.TextField()
#     re_suggestion_mgt = models.TextField()
