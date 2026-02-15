from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogUser(User):
    avatar = models.ImageField(upload_to='images',default='person.png')  