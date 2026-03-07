from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver




class BlogUser(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/avatars',default='def_avatar.png')   
    mobile = models.CharField(max_length=11,null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        BlogUser.objects.create(user=instance)



