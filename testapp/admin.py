from django.contrib import admin
from testapp.models import job

# Register your models here.
class jobAdmin(admin.ModelAdmin):
    list_display=["id","jobname","jobid","jobsal","jobage"]

admin.site.register(job,jobAdmin)
