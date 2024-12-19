from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def Home(request):
    now = datetime.datetime.now()
    subject = "Time is {}".format(now)
    return render(request,'Home.html', {'subject':subject})


def Nextpage(request):
    title = "hello Thailand this is project"
    return render(request,'index.html', {'title':title})