from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(
        null=True,
        blank=True)   
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("organize:post_detail",kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp","-updated"]

class Leader(models.Model):
    title = models.CharField(max_length=100)
    event_link = models.ManyToManyField(Event)

    def __str__(self):
        return self.title

class Volunteer(models.Model):
    title = models.CharField(max_length=100)
    leader_link = models.ManyToManyField(Leader)

    def __str__(self):
        return self.title
    
    