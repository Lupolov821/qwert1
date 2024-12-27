from django.shortcuts import render

def index(request):
    return render(request, "main4/index.html")

def page1(request):
    return render(request, "main4/page1.html")

def page2(request):
    return render(request, "main4/page2.html")

def page3(request):
    return render(request, "main4/page3.html")

def page4(request):
    return render(request, "main4/page4.html")




