from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'main/index.html', context)

def page(request):
    context={}
    return render(request,'main/inner-page.html', context)