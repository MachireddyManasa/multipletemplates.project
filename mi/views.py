from django.shortcuts import render

# Create your views here.
def rohitsharma(request):
    d={'name':'rohit','age':'36'}
    return render(request,'rohitsharma.html',context=d)
