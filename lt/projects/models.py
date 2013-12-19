from django.db import models

# Create your models here.

class Projects(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='projects')
	site_url = models.CharField(max_length=250, null=True, blank=True)
	github_url = models.CharField(max_length=250, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'Projects'

	def __unicode__(self):
		return self.name + ' - ' + self.site_url