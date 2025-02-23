from django.shortcuts import render
from .models import ServiceRequest

def request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'request_list.html', {'requests': requests})
