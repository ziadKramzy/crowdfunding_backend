from django.db import models
from django.utils import timezone
from users.models import User

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(default=lambda: timezone.now().date())
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title
