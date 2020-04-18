from django.db import models
from django.contrib.auth.models import User




CATEGORY_CHOICE = [('Customer', 'Customer'), ('Company', 'Company')]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_category = models.CharField(max_length=100 , default='Customer')

    def __str__(self):
        return f'{self.user.username} Profile'
