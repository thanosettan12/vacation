from django.http import HttpResponse
from django.shortcuts import render
from.models import property_agent
# Create your views here.
def demo(request):
    obj=property_agent.objects.all()
    return render(request,"index.html",{'result':obj})
