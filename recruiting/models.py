from django.db import models


class Recruiting_list(models.Model):
    company_name = models.CharField(max_length=100, db_column='company_name')
    job = models.CharField(max_length=100, db_column='job')
    company_intro = models.TextField()
    main_duties = models.TextField()
    requirments = models.TextField()
    stack = models.TextField()
    desirable_skills= models.TextField()
    employee_benefits = models.TextField()
    address = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.pk}    -    {self.company_name}'
    
    def get_absolute_url(self):
        return f'/recruiting/{self.pk}'
    




