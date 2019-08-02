from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Program, Speaker,sponsors,pastspeakers,post

# Create your views here.
def index(request):
    speaker_table=Speaker.objects.all()
    program_table=Program.objects.all()
    sponsors_table=sponsors.objects.all()
    post_table=post.objects.filter(status=1).order_by('-created_on')[:3]
    context={"index":"active","speaker":speaker_table,"program":program_table, "sponsors":sponsors_table, "post":post_table }
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
