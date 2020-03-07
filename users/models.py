from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = user_directory_path, blank = True)
    
    def __str__(self):
        return self.user.username
