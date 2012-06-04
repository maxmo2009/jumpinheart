from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User)
	use_gravt = models.BooleanField(default=True)
	avt_uri = models.CharField(max_length=50)
# Create your models here.
