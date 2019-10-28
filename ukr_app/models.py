from django.db import models
from django.urls import reverse
# Create your models here.


class Links(models.Model):
    url = models.URLField(max_length=200)
    status = models.BooleanField(default=False)
    interval = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('link_detail', kwargs={'pk': self.pk})
