from django.http import HttpResponse
from django.shortcuts import render

# html page :
def homePage(request):
    #data dictionary to pass data to html views:
    data = {
        
    }
    return render(request,"index.html")

#other pages :

def aboutus(request):
    return HttpResponse("Welcome to ABOUT-US</b>")

def course(request):
    return HttpResponse("Welcome to COURSE")




# fun for dynamic url :
def courseInfo1(request,cinfo):
    return HttpResponse(cinfo)

def courseInfo2(request,cinfo):
    return HttpResponse(cinfo)

def courseInfo3(request,cinfo):
    return HttpResponse(cinfo)