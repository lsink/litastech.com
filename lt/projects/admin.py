from django.contrib import admin

from .models import Projects

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Projects, ProjectsAdmin)
