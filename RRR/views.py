from django.shortcuts import render
# Create your views here.
def kak(request):
    return render(request,'first.html')
def story(request):
    return render(request,'story.html')
def Goal(request):
    return render(request,"Goal.html")
