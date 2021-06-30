from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birthdate = models.DateField('birthdate',null=True,blank=True)
    phone_number = models.IntegerField(blank=False,null=False,unique=True)

    class Meta:
        verbose_name='profile'
        verbose_name_plural = 'profiles'
    def __str__(self):
        return self.user.username
        

