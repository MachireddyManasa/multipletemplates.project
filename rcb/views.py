from django.shortcuts import render

# Create your views here.
def kohli(request):
    d={'name':'kohli','age':'35'}
    return render(request,'kohli.html',context=d)
