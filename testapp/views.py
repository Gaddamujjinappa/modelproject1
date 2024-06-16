from django.shortcuts import render
from testapp.models import job

# Create your views here.
def job_view(request):
    hirect=job.objects.all()
    return render(request,"index.html",{'hirect':hirect})
    

