from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Animal

# Create your models here.
class Animal(models.Model):
	name = models.TextField()
	slug = models.SlugField(max_length=250)
	adopted = models.DateTimeField(auto_now_add=True)
	publish = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.name