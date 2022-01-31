from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIP = 2
GUEST = 3
USER = 4
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIP, 'VIP'),
    (GUEST,'GUEST'),
    (USER, 'USER')
)
MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)


class CustomUser(User):
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя', default=USER)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, verbose_name='phone_number')
    age = models.IntegerField(blank=True)
    height=models.FloatField(blank=True)
    weight=models.FloatField(blank=True)
    user_job=models.CharField(max_length=15,blank=True)