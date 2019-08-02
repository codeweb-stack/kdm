from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Speaker

# Create your views here.
def index(request):
    speaker_table=Speaker.objects.all()
    context={"index":"active","speaker":speaker_table }
    return render(request,'kdm/index.html',context)

def about(request):
    context={"about":"active"}
    return render(request,'kdm/about.html',context)

def speakers(request):
    context={"speakers":"active"}
    return render(request, 'kdm/speakers.html',context)

def news(request):
    context={"news":"active"}
    return render(request, 'kdm/news.html',context)

def contact(request):
    context={"contact":"active"}
    return render(request,'kdm/contact.html',context)

def free_tickets(request):
    context={"tickets":"active"}
    return render(request, 'kdm/free-tickets.html',context)
