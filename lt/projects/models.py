from django.db import models

# Create your models here.

class Projects(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='projects')
	github_url = models.CharField(max_length=250, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)