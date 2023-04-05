from django.db import models
from django.contrib.auth.models import User


education = (
    ('NURSERY','NURSERY'),
    ('PRIMARY','PRIMARY'),
    ('SECONDARY','SECONDARY'),
    ('DEGREE','DEGREE'),
    ('MASTERS','MASTERS'),
    ('PHD','PHD')
)

ids = (
    ('NATIONAL IDENTITY CARD','NATIONAL IDENTITY CARD'),
    ('VOTERS CARD','VOTERS CARD'),
    ('DRIVERS LICENCE','DRIVERS LICENCE'),
    ('PASSPORT','PASSPORT')

)

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    other_names = models.CharField(max_length=20,null=True)
    profile_pics = models.ImageField(default='',upload_to='pics',null=True)
    phone_number = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    gendre = models.CharField(max_length=10,choices=(('MALE','MALE'),('FEMALE','FEMALE')),null=True)
    state_of_origin = models.CharField(max_length=20,null=True)
    lga_origin = models.CharField(max_length=100,null=True)
    scheme_name = models.CharField(max_length=100,null=True)
    year_of_application = models.CharField(max_length=4,null=True)
    residencial_address = models.CharField(max_length=100,null=True)
    state_of_residence = models.CharField(max_length=20,null=True)
    lga_residence = models.CharField(max_length=100,null=True)
    highest_level_of_education = models.CharField(max_length=20,choices=education,null=True)
    id_type = models.CharField(max_length=100,choices=ids,null=True)
    id_number = models.IntegerField(null=True)
    id_image = models.ImageField(upload_to='pics',null=True)
    bvn = models.IntegerField(null=True)
    bank_acccount_number = models.IntegerField(null=True)
    bank_name = models.CharField(max_length=50,null=True)
    account_name = models.CharField(max_length=50,null=True)
    
   

    def __str__(self) -> str:
        return f'{self.user}'