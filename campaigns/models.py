from django.db import models
from django.utils import timezone
from users.models import User
from django.utils.timezone import now
from cloudinary.models import CloudinaryField

def today():
    return now().date()

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    start_date = models.DateField(default=today)
    end_date = models.DateField()
    image = CloudinaryField('image', blank=True, null=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title
