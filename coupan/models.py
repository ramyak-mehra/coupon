from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from users.models import Profile
# Create your models here.


class Coupan(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default = (timezone.now() + timezone.timedelta(days=1)))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(Profile)
    code = models.CharField(max_length=200)
   

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('coupan-detail' , kwargs={'pk' : self.pk})
